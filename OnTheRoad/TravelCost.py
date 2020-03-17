
from OnTheRoad import Location

from flask.logging import default_handler
import logging
import numpy as np


logger = logging.getLogger(__name__.split('.')[0])
logger.addHandler(default_handler)


# TODO: Have to incorporate Google Flights API

class TravelCost:
    MAX_VAL = np.inf

    @staticmethod
    def getTravelCost(startLoc, endLoc):
        travelCost = TravelCost(startLoc, endLoc)
        return travelCost.cost()

    @staticmethod
    def cost(startLoc, endLoc):
        return TravelCost.getDistanceBetween(startLoc, endLoc)

    @staticmethod
    def getDistanceBetween(startLoc, endLoc):
        travelMode = "transit"
        [dist_meters, duration_seconds] = TravelCost.getDistanceByMode(startLoc, endLoc, travelMode)
        if dist_meters == TravelCost.MAX_VAL:
            travelMode = "driving"
            [dist_meters, duration_seconds] = TravelCost.getDistanceByMode(startLoc, endLoc, travelMode)
        return [dist_meters, duration_seconds]

    @staticmethod
    def getDistanceByMode(startLoc, endLoc, travelMode):
        source_address = startLoc.getAddress()
        dest_address = endLoc.getAddress()
        #mode = "transit"

        # Prepare Caching Directory
        import os
        temp_dir = "./data_cache/"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        filename = temp_dir + startLoc.getShortName() + "-" + endLoc.getShortName() + ".obj"
        #filename = temp_dir + source_address.replace(" ", "_") + "-" + dest_address.replace(" ", "_") + ".obj"

        import urllib.parse
        import urllib.request
        import os.path

        if os.path.isfile(filename):
            #print("LOADING FROM CACHE: {}".format(filename))
            j = loadObj(filename)
        else:
            import os
            API_KEY = os.environ['GOOG_API_KEY']
            source_address = urllib.parse.quote_plus(source_address)
            dest_address = urllib.parse.quote_plus(dest_address)

            my_url = "/maps/api/directions/json?origin={}&destination={}&sensor=false&mode={}".format(source_address, dest_address, travelMode)
            url_addr = "https://maps.googleapis.com%s" % my_url
            url_addr += "&key=" + API_KEY

            # Make actual request
            data = urllib.request.urlopen(url_addr)

            #import urllib3
            #opener = urllib.build_opener()
            #opener.addheaders = [('Referer', 'https://johnstratoudakis.com')]
            #data = opener.open(url_addr)

            # Response
            resData = data.read()
            import chardet
            import json
            j = json.loads(resData.decode(chardet.detect(resData)["encoding"]))
            #j = json.loads(resData)

            if 'error_message' in j:
                print("There is an error message embedded in the response.")
                print("Error Message: {}".format(j["error_message"]))
                print("Status: {}".format(j["status"]))
#                print("j: {}".format(j))
                return [TravelCost.MAX_VAL, TravelCost.MAX_VAL]
            elif j['status'] == 'ZERO_RESULTS':
                print("ZERO_RESULTS.")
                #dumpToScreen(j)
                return [TravelCost.MAX_VAL, TravelCost.MAX_VAL]
            #else:
                #print("NO ERROR")

#        dumpToScreen(j)
        dumpObj(j, filename)
        dist_meters = j['routes'][0]['legs'][0]['distance']['value']
        duration_seconds = j['routes'][0]['legs'][0]['duration']['value']
        #print("dist_meter: {}".format(dist_meters))
        return [dist_meters, duration_seconds]

def dumpToScreen(json_obj):
        print(80 * "-")
        print("DUMP OF DATA____________2")
        print("type(j): {}".format(type(json_obj)))
        import json
        print(json.dumps(json_obj, indent=4))
        print(80 * "-")

def dumpObj(raw_obj, filename):
    import pickle
    with open(filename, "wb") as fout:
        pickle.dump(raw_obj, fout)

#    from pprint import pprint
#    with open(filename + ".json", "w", encoding="utf-8") as fout_json:
#    #fout = open(filename + ".json", "w")
#        pprint(raw_obj, stream=fout_json, indent=4)

def loadObj(filename):
    data = None
    import pickle
    with open(filename, "rb") as fin:
        data = pickle.load(fin)
    return data

