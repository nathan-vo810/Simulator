from random import uniform

from ApplianceCycle import WashingMachineCycle
from ApplianceProfile import ApplianceProfile
from DailyFrequency import DailyFrequency

import const


class Appliance:
    # Basic data that all appliance probaly need.
    def __init__(self, applianceName):
        self.applianceName = applianceName
        self.usingDailyFrequency = DailyFrequency(applianceName).__getattribute__('dailyUsingFrequency')
        self.applianceProfile = ApplianceProfile(applianceName)
        self.leftCycleTime = 0
        self.leftRestartDelay = 0

    # def __init__(self, numberOfOccupant, applianceName):
    #     self.applianceName = applianceName
    #     self.numberOfOccupant = numberOfOccupant
    #     self.usingDailyFrequency = generateUsingDailyFrequency(applianceName)
    #     self.applianceProfile = ApplianceProfile(applianceName)

    def isApplianceOff(self):
        return self.leftCycleTime == 0

    def isApplianceInDelayForTurnOff(self):
        return self.leftRestartDelay != 0

    def isApplianceAvailable(self, occupants):
        # Dummy prob for testing
        probabilityFromOccupant = occupants/const.Const.MAX_ACTIVE_OCCUPANTS
        randomProbabilityForStartingApplicance = uniform(0,1)
        return probabilityFromOccupant >= randomProbabilityForStartingApplicance

    def noActiveOccupants(self, occupants):
        return occupants == 0

    def isWashingMachine(self):
        return self.applianceName == const.Const.WASHING_MACHINE_NAME

    def hasNoDelay(self):
        return self.applianceProfile.__getattribute__('restartDelay') == 0

    def doStart(self):
        self.leftCycleTime = self.applianceProfile.__getattribute__('cycleTime')

    def doStop(self):
        self.leftRestartDelay = self.applianceProfile.__getattribute__('restartDelay')
        if self.leftRestartDelay > 0: self.leftRestartDelay = self.leftRestartDelay - 1

    def getPowerUsageDependOnState(self):
        return self.applianceProfile.__getattribute__('onPower')

    def calculate_power_consumption(self, occupants):
        # print('A')
        if self.isApplianceOff() and not self.isApplianceInDelayForTurnOff() and self.isApplianceAvailable(occupants):
            # print('B')
            self.doStart()
            return self.applianceProfile.__getattribute__('onPower')
        elif self.isApplianceOff():
            # print('C')
            self.leftCycleTime = self.leftCycleTime - 1
            if not self.isApplianceOff():
                return self.getPowerUsageDependOnState()
            elif self.hasNoDelay() and self.isApplianceAvailable(occupants):
                self.doStart()
                return self.applianceProfile.__getattribute__('onPower')
            else:
                self.doStop()
                return self.applianceProfile.__getattribute__('offPower')
        elif self.isApplianceInDelayForTurnOff():
            # print('D')
            self.leftRestartDelay = self.leftRestartDelay - 1
        return self.applianceProfile.__getattribute__('offPower')
    # Get power of the variance.
    def getPower(self):
        return self.powerConsumption

    def getAppianceName(self):
        return self.applianceName


class WashingMachine(Appliance):
    # Basic data from the parent class
    # +
    # special data for Washing Machine since this is a state machine.
    def __init__(self, numberOfOccupant, applianceName):
        Appliance.__init__(self, applianceName)
        self.powerCycle = WashingMachineCycle(numberOfOccupant).__getattribute__('cycleProfile')
        self.numberOfOccupant = numberOfOccupant

    def getAppianceName(self):
        return self.applianceName

    def getPowerUsageDependOnState(self, leftCycleTime):
        cycleProfile = self.powerCycle
        for i in range(len(cycleProfile)):
            if i%3 == 0 and leftCycleTime <= cycleProfile[i]:
                return cycleProfile[i+2]

    def calculate_power_consumption(self, occupants):
        # print('A')
        # print(self.leftRestartDelay)
        if self.isApplianceOff() and not self.isApplianceInDelayForTurnOff() and self.isApplianceAvailable(occupants):
            # print('B')
            self.doStart()
            # Noise is for the diversity of the data, more research is needed!!!!
            return self.applianceProfile.__getattribute__('onPower') + self.generateRandomNoise()
        elif not self.isApplianceOff():
            # print('C')
            if self.noActiveOccupants(occupants) and not self.isWashingMachine():
                # print('C1')
                return self.applianceProfile.__getattribute__('offPower') + self.generateRandomSmallNoise()
            else:
                # print('C2')
                self.leftCycleTime = self.leftCycleTime - 1
                if not self.isApplianceOff():
                    return self.getPowerUsageDependOnState(self.leftCycleTime) + self.generateRandomNoise()
                elif self.hasNoDelay() and self.isApplianceAvailable(occupants):
                    self.doStart()
                    return self.applianceProfile.__getattribute__('onPower') + self.generateRandomNoise()
                else:
                    self.doStop()
                    return self.applianceProfile.__getattribute__('offPower') + self.generateRandomSmallNoise()
        elif self.isApplianceInDelayForTurnOff():
            # print('D')
            self.leftRestartDelay = self.leftRestartDelay - 1
        return self.applianceProfile.__getattribute__('offPower') + self.generateRandomSmallNoise()

    def generateRandomSmallNoise(self):
        return uniform(0, 1)

    def generateRandomNoise(self):
        return uniform(0, 2)