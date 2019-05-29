
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
