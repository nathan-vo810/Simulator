import argparse

import Plotter
import const
from Appliance import WashingMachine
from DataWriter import DataWriter
from OccupancyModel import OccupancyModel
from Output import Output
from input import Input


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
    # print(input)

    # Dummy get the number of people at home at specific time interval (Need MarkovChain or something else someday)
    occupancyModel = OccupancyModel(input.occupantNumber)

    # Dummy implement for only washing machine
    washingMachine = WashingMachine(input.occupantNumber, const.Const.WASHING_MACHINE_NAME)

    # Simulate energy consumption of washing machine
    outputEnergyConsumption = Output(occupancyModel.__getattribute__('occupancyModel'), washingMachine)

    # print('Output Energy Consumption :')
    # print(outputEnergyConsumption.__getattribute__('output'))

    # Write output to the file csv
    DataWriter.writeCsvFile(outputEnergyConsumption.__getattribute__('output'))

    #Plot the simulate data
    Plotter.plot('output.csv', 0)