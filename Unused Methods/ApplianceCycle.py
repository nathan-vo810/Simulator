import DataReader
import const


class ApplianceCycle:
    pass


def generateWashingMachineCycle(numberOfOccupant):
    fileName = const.Const.WASHING_MACHINE_CYCLE_FILENAME
    rowLevel = 0
    if numberOfOccupant > 3: rowLevel = 1
    return DataReader.readCsVFile(fileName, rowLevel)


class WashingMachineCycle(ApplianceCycle):
    def __init__(self, numberOfOccupant):
        self.cycleProfile = generateWashingMachineCycle(numberOfOccupant)
        # print("Cycle Profile: ")
        # print(self.cycleProfile)