import argparse
from random import randint

import const
from Appliance import WashingMachine
from input import Input


def generateOccupancyModel(occupants):
    return randint(0, occupants)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--o',
                        help='The current number of occupants (must be from 0 to 3). Default value is 1 person', \
                        choices=[0, 1, 2, 3],
                        nargs='?',
                        const=const.Const.DEFAULT_OCCUPANTS,
                        type=int,
                        default=const.Const.DEFAULT_OCCUPANTS,
                        metavar='Occupant')
    parser.add_argument('-wk',
                        help='Specify if current time is weekend or not',
                        action='store_true')
    parser.add_argument('--m',
                        help='The current month (must be from 1 to 12). Default value is 1 (January)', \
                        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        nargs='?',
                        const=const.Const.DEFAULT_MONTH,
                        type=int,
                        default=const.Const.DEFAULT_MONTH,
                        metavar='Month')
    args = parser.parse_args()

    # Dummy input
    input = Input(args.o, args.wk, args.m, const.Const.DEFAULT_INTERVAL_TIME)

    # Check input
    print(input)

    # Dummy get the number of people at home at specific time interval
    occupancyModel = [generateOccupancyModel(input.occupantNumber) for i in range(const.Const.DEFAULT_ARRAY_LENGTH)]


    # Dummy implement for only washing machine
    washingMachine = WashingMachine(input.occupantNumber, const.Const.WASHING_MACHINE_NAME)