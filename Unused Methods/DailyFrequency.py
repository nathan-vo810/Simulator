import DataReader

import const


def generateDailyFrequency(applianceName):
    # Take data from the file: activityStats.csv and find the data for it
    # For now just use dummy data archieve from it manually
    # These numbers are from LAUNDRY in activityStats.csv
    # for Weekend
    # and number of occupants = 3
    if applianceName == const.Const.WASHING_MACHINE_NAME:
        fileName = const.Const.ACTIVITY_STATS_FILE_LOCATION
        rowLevel = 20
    return DataReader.readCsVFile(fileName, rowLevel)


class DailyFrequency:
    def __init__(self, applianceName):
        self.dailyUsingFrequency = generateDailyFrequency(applianceName)
        # print("Daily Using Frequency: ")
        # print(self.dailyUsingFrequency)