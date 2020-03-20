
from OnTheRoad import Location

from flask.logging import default_handler
import chardet
import json
import logging
import numpy as np

import urllib.parse
import urllib.request
import os.path

logger = logging.getLogger(__name__.split('.')[0])
logger.addHandler(default_handler)

class TravelCost(object):
    MAX_VAL = np.inf

    @staticmethod
    def getDistanceBetween(startLoc, endLoc):
        logger.debug(f"getDistanceBetween({startLoc} -> {endLoc})")

        travelMode = "transit"
        [dist_meters, duration_seconds] = TravelCost.getDistanceByMode(startLoc, endLoc, travelMode)
        if dist_meters == TravelCost.MAX_VAL:
            travelMode = "driving"
            [dist_meters, duration_seconds] = TravelCost.getDistanceByMode(startLoc, endLoc, travelMode)
        return [dist_meters, duration_seconds]

    @staticmethod
    def getDistanceByMode(startLoc, endLoc, travelMode):
        logger.debug(f"getDistanceByMode({startLoc} -> {endLoc} via {travelMode}")

        source_address = startLoc.getAddress()
        dest_address = endLoc.getAddress()
        #mode = "transit"

        # Prepare Caching Directory
        import os
        temp_dir = "./data_cache/"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        filename = temp_dir + startLoc.getShortName() + "-" + endLoc.getShortName() + ".obj"

        if os.path.isfile(filename):
            logger.debug(" + Loading from cache: {}".format(filename))
            j = loadObj(filename)
        elif True:
            logger.info("SKIPPING")
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

            # Response
            resData = data.read()
            j = json.loads(resData.decode(chardet.detect(resData)["encoding"]))
            #j = json.loads(resData)

            logger.info(80 * "r")
            logger.info("DUMP OF DATA____________3")
            if 'error_message' in j:
                print("There is an error message embedded in the response.")
                print("Error Message: {}".format(j["error_message"]))
                print("Status: {}".format(j["status"]))
#                print("j: {}".format(j))
                return [TravelCost.MAX_VAL, TravelCost.MAX_VAL]
            elif j['status'] == 'ZERO_RESULTS':
                print("ZERO_RESULTS.")
                print("Start: {}".format(startLoc.getName()))
                print("Stop: {}".format(endLoc.getName()))
                dumpToScreen(j)
                return [TravelCost.MAX_VAL, TravelCost.MAX_VAL]
            else:
                print("NO ERROR")
                dumpToScreen(j)

#        dumpToScreen(j)
        dumpObj(j, filename)
        dist_meters = j['routes'][0]['legs'][0]['distance']['value']
        duration_seconds = j['routes'][0]['legs'][0]['duration']['value']
        #print("dist_meter: {}".format(dist_meters))

        logger.debug(f" <- ({dist_meters} meters, {duration_seconds} seconds)")
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

    import json
    with open(filename + ".json", "w", encoding="utf-8") as fout_json:
        fout_json.write(json.dumps(raw_obj, indent=4))
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