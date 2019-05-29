

class TravelCost:
    def __init__(self, startLoc, endLoc):
        self.startLoc = startLoc
        self.endLoc = endLoc

    def cost(self):
        return self.getDistanceBetween(self.startLoc.getAddress(), self.endLoc.getAddress())

    def getDistanceBetween(self, source_address, dest_address):
        # Prepare Caching Directory
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
            mode = "transit"
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
            if 'error_message' in j:
                print(f"There is an error message embedded in the response:\n\t {j['error_message']}")
            else:
                dumpObj(j, filename)

        dist_meters = j['routes'][0]['legs'][0]['distance']['value']
        duration_seconds = j['routes'][0]['legs'][0]['duration']['value']
        return [dist_meters, duration_seconds]

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

