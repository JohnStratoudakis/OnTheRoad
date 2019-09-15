from Travel import Combinations
from Travel import Location

class TravelCost:
    MAX_VAL = 9999999

    def __init__(self, startLoc, endLoc):
        self.startLoc = startLoc
        self.endLoc = endLoc

    def __init__(self, paths):
        print("Add paths")
        print("type(paths): " + str(type(paths)) )

    @staticmethod
    def getTravelCost(startLoc, endLoc):
        travelCost = TravelCost(startLoc, endLoc)
        return travelCost.cost()

    def cost(self):
        return TravelCost.getDistanceBetween(self.startLoc, self.endLoc)

    @staticmethod
    def allCosts(inCities : Location.Location):
        allPaths = Combinations.Combinations.getAllPaths( inCities )

        allCosts = []
        for path in allPaths:
            #cost = TravelCost(path)
            print("Adding path: {}".format(path))
            allCosts.append(path)

        return allCosts

    @staticmethod
    def getDistanceBetween(startLoc, endLoc):
        source_address = startLoc.getAddress()
        dest_address = endLoc.getAddress()
        mode = "transit"

        # Prepare Caching Directory
        import os
        temp_dir = "./data_cache/"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        filename = temp_dir + source_address.replace(" ", "_") + "-" + dest_address.replace(" ", "_") + ".obj"

        import urllib.parse
        import urllib.request
        import os.path

        if os.path.isfile(filename):
            print(f"LOADING FROM CACHE: {filename}")
            j = loadObj(filename)
        else:
            import os
            API_KEY = os.environ['GOOG_API_KEY']
            source_address = urllib.parse.quote_plus(source_address)
            dest_address = urllib.parse.quote_plus(dest_address)

            my_url = f"/maps/api/directions/json?origin={source_address}&destination={dest_address}&sensor=false&mode={mode}" 
            url_addr = "https://maps.googleapis.com%s" % my_url
            url_addr += "&key=" + API_KEY

            # Make actual request
            data = urllib.request.urlopen(url_addr)
            print(f'Request data.status = {data.status}')
            resData = data.read()
            #print(type(data))
            import json
            j = json.loads(resData)
            if 'error_message' in j or j['status'] == 'ZERO_RESULTS':
                print("ERROR")
                print(f"There is an error message embedded in the response:\n\t {j['error_message']}")
                return [TravelCost.MAX_VAL, TravelCost.MAX_VAL]
            else:
                print("NO ERROR")
                dumpObj(j, filename)
        #dumpToScreen(j)

        dist_meters = j['routes'][0]['legs'][0]['distance']['value']
        duration_seconds = j['routes'][0]['legs'][0]['duration']['value']
        return [dist_meters, duration_seconds]

def dumpToScreen(json_obj):
        print(80 * "-")
        print("DUMP OF DATA")
        print("type(j): {}".format(type(json_obj)))
        print(json_obj)
        print(80 * "-")

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

