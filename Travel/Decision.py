class Decision:

    def __init__(self, ThresholdMiles=5, ThresholdTime=20):
        self.thresholdMiles = ThresholdMiles
        self.thresholdTime = ThresholdTime

    def shouldCarPoolDistance(self, guestA, guestB):
        if (guestA.distanceTo(guestB) - guestA.distanceToCeremony) > self.thresholdMiles:
            return False
        return True

    def shouldCarPoolTime(self, guestA, guestB):
        if (guestA.timeTo(guestB) - guestA.timeToCeremony) > self.thresholdTime:
            return False
        return True

