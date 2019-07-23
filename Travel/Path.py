
class Path(object):

    def __init__(self, startCity, stopCity):
        self.startCity = startCity
        self.stopCity = stopCity

    def getStartCity(self):
        return self.startCity

    def getStopCity(self):
        return self.stopCity