
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

    def __str__(self):
        return f"{self.name}"