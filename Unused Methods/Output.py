def runSimulation(occupancyModel, washingMachine):
    # for occupants in occupancyModel:
    #     print(washingMachine.calculate_power_consumption(occupants))
    return [washingMachine.calculate_power_consumption(occupants) for occupants in occupancyModel]


class Output:
    def __init__(self, occupancyModel, washingMachine):
        self.output = runSimulation(occupancyModel, washingMachine)