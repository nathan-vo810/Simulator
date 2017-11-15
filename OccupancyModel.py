from random import randint

import const


def generateOccupancyModel(occupants, i):
    return randint(0, occupants)


class OccupancyModel:
    def __init__(self, occupants):
        self.occupancyModel = [generateOccupancyModel(occupants,i) for i in range(const.Const.DEFAULT_ARRAY_LENGTH)]
