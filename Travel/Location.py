
class Location:
    def __init__(self, name, shortName, address):
        self.name = name
        self.shortName = shortName
        self.address = address 

    def getName(self):
        return self.name

    def getShortName(self):
        return self.shortName

    def getAddress(self):
        return self.address

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

    def __str__(self):
        return f"{self.name}"
