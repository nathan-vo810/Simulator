import const


class ApplianceProfile:
    def __init__(self, applianceName):
        # Take data from the file: appliances.csv and find the data for it
        # For now just use dummy data archieve from it manually
        # These numbers are from WASHING MACHINE in appliances.csv
        if applianceName == const.Const.WASHING_MACHINE_NAME:
            self.onPower = 217.7101  # Mean cycle power
            # = Mean cycle power * mean cycle length / new mean cycle length
            self.offPower = 1  # Standby power
            self.cycleTime = 74  # Mean cycle length #I adjust this one temporarily to match
            # with the number from the new research file WashingMachineCycle
            self.restartDelay = 0  # Delay-restart-after cycle
            self.scaleFactor = 0.0517795  # Calibration scalar
