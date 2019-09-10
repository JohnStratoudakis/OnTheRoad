
class Path(object):

    allStops = None

    def __init__(self, stops):
        #print("PATH: {}, LEN(STOPS): {}".format( stops, len(stops)  ))
        if len(stops) == 1:
            self.startCity = stops[0]
            self.stopCity = stops[0]
        else:
            self.startCity = stops[0]
            self.stopCity = stops[ len(stops)-1 ]
        self.allStops = stops

    def getStartCity(self):
        return self.startCity

    def getStopCity(self):
        return self.stopCity

    def __str__(self):
        return "TO_STRING"
