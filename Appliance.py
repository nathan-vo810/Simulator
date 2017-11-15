from ApplianceCycle import WashingMachineCycle
from ApplianceProfile import ApplianceProfile
from DailyFrequency import DailyFrequency


class Appliance:
    #Basic data that all appliance probaly need.
    def __init__(self, applianceName):
        self.applianceName = applianceName
        self.usingDailyFrequency = DailyFrequency(applianceName)
        self.applianceProfile = ApplianceProfile(applianceName)

    # def __init__(self, numberOfOccupant, applianceName):
    #     self.applianceName = applianceName
    #     self.numberOfOccupant = numberOfOccupant
    #     self.usingDailyFrequency = generateUsingDailyFrequency(applianceName)
    #     self.applianceProfile = ApplianceProfile(applianceName)

    def getAppianceName(self):
        return self.applianceName;

class WashingMachine(Appliance):
    #Basic data from the parent class
    # +
    # special data for Washing Machine since this is a state machine.
    def __init__(self, numberOfOccupant, applianceName):
        Appliance.__init__(self, applianceName)
        self.powerCycle = WashingMachineCycle(numberOfOccupant)
        self.numberOfOccupant = numberOfOccupant

    def getAppianceName(self):
        return self.applianceName;
