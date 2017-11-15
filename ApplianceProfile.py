import const


def find_appliance_profile_base_on_the_appliance_name(applianceProfile, applianceName):
    # Take data from the file: appliances.csv and find the data for it
    # For now just use dummy data archieve from it manually
    # These numbers are from WASHING MACHINE in appliances.csv
    if applianceName == const.Const.WASHING_MACHINE_NAME:
        applianceProfile.onPower = 406 #Mean cycle time
        applianceProfile.offPower = 1 #Standby power
        applianceProfile.cycleTime = 138 #Mean cycle length
        applianceProfile.restartDelay = 0 #Delay-restart-after cycle
        applianceProfile.scaleFactor = 0.0517795 #Calibration scalar


class ApplianceProfile:
    def __init__(self, applianceName):
        self.data = find_appliance_profile_base_on_the_appliance_name(self, applianceName)

    def getData(self):
        return self.data;