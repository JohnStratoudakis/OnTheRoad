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

