
class TravelCost:
    pass


def dumpObj(obj, filename):
    import pickle
    with open(filename, "wb") as fout:
        pickle.dump(obj, fout)

    from pprint import pprint
    with open(filename + ".json", "w") as fout_json:
    #fout = open(filename + ".json", "w")
        pprint(obj, stream=fout_json, indent=4)

def loadObj(filename):
    data = None
    import pickle
    with open(filename, "rb") as fin:
        data = pickle.load(fin)
    return data

def getDistanceBetween(source_address, dest_address):
    import os
    temp_dir = "./data_tmp/"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    filename = temp_dir + source_address.replace(" ", "_") + "-" + dest_address.replace(" ", "_") + ".obj"

    import urllib.parse
    import urllib.request
    import os.path
    if os.path.isfile(filename):
        j = loadObj(filename)
    else:
        my_url = "/maps/api/directions/json?origin=%s&destination=%s&sensor=false&mode=driving" % (
                urllib.parse.quote_plus(source_address),
                urllib.parse.quote_plus(dest_address) )
        url_addr = "http://maps.googleapis.com%s" % my_url

        data = urllib.request.urlopen(url_addr)
        import json
        j = json.loads(data.read())
        dumpObj(j, filename)

    dist = j['routes'][0]['legs'][0]['distance']['text'] 
    dist_meters = j['routes'][0]['legs'][0]['distance']['value'] 
    duration = j['routes'][0]['legs'][0]['duration']['text']
    duration_seconds = j['routes'][0]['legs'][0]['duration']['value']

    return [dist_meters, duration_seconds]

class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address 

    def getName(self):
        return self.name

    def calculateDistances(self, allGuests, ceremony):
        self.paths = {}
        for guest in allGuests:
            if self.address != guest.address:
                print("\t {0} and {1}".format(self.address, guest.address))
                results = getDistanceBetween(self.address, guest.address)
                print("\t\t {} meters {} seconds".format(results[0], results[1]))
                self.paths[guest.getName()] = results
        self.ceremony = getDistanceBetween(self.address, ceremony.address)
        print("\tCeremony: {} meters {} seconds".format(self.ceremony[0], self.ceremony[1]))

class CarPool:
    def __init__(self, allGuests, ceremony):
        self.allGuests = allGuests
        self.ceremony = ceremony

    def getPaths(self):
        carPool = [ self.allGuests[2], self.allGuests[0] ]
        solo = [ self.allGuests[1] ]

        for guest in self.allGuests:
            #print("Calculating path for guest: {}".format(guest.getName()))
            guest.calculateDistances(self.allGuests, self.ceremony)


        #guestCombinations = list(itertools.permutations(self.allGuest
#        for guest in self.allGuests:
#            currentGuest = guest
#            restOfGuests = set(self.allGuests)
#            restOfGuests.remove(currentGuest)
#            print("Current guest: {}".format(currentGuest.getName()))
#            solo = set(currenctGuest)
# J->C, [P->L->C]
# J->C, [L->P->C]

        paths = Paths( carPool, solo )
        return paths

# Paths contains the results - an ordered list of who should carpool
# and a set of who should drive solo
class Paths:
    def __init__(self, carPool, solo):
        self.carPool = carPool
        self.solo = solo

    def shouldCarPool(self):
        return self.carPool

    def shouldDriveSolo(self):
        return self.solo


class Decision:

    def __init__(self, ThresholdMiles=5, ThresholdTime=20):
        self.thresholdMiles = ThresholdMiles
        self.thresholdTime = ThresholdTime

    def shouldCarPoolDistance(self, guestA, guestB):
        if (guestA.distanceTo(guestB) - guestA.distanceToCeremony) > self.thresholdMiles:
            return False
        return True

    def shouldCarPoolTime(self, guestA, guestB):
        if (guestA.timeTo(guestB) - guestA.timeToCeremony) > self.thresholdTime:
            return False
        return True


