
class TravelCost:
    def __init__(self, startLoc, endLoc):
        self.startLoc = startLoc
        self.endLoc = endLoc

    def cost(self):
        self.getDistanceBetween(self.startLoc.getAddress(), self.endLoc.getAddress())

    def getDistanceBetween(self, source_address, dest_address):
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
            import os
            API_KEY = os.environ['GOOG_API_KEY']
            my_url = "/maps/api/directions/json?origin=%s&destination=%s&sensor=false&mode=driving" % (
                    urllib.parse.quote_plus(source_address),
                    urllib.parse.quote_plus(dest_address) )
            url_addr = "https://maps.googleapis.com%s" % my_url
            url_addr += "&key=" + API_KEY

            data = urllib.request.urlopen(url_addr)
            print(f'data.status = {data.status}')
            resData = data.read()
            #print(f'resData = {resData}')

            #data = urllib.request.urlopen(url_addr)
            print(type(data))
            import json
            j = json.loads(resData)
            #j = json.loads(data.read())
            if 'error_message' in j:
                print(f"There is an error message embedded in the response:\n\t {j['error_message']}")
            else:
                dumpObj(j, filename)

            #dist = j['routes'][0]['legs'][0]['distance']['text'] 
            #dist_meters = j['routes'][0]['legs'][0]['distance']['value'] 
            #duration = j['routes'][0]['legs'][0]['duration']['text']
            #duration_seconds = j['routes'][0]['legs'][0]['duration']['value']

        return [0, 0]
        #return [dist_meters, duration_seconds]

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


