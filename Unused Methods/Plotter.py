
import DataReader
import matplotlib.pyplot as plt
import numpy as np


def plot(fileName, columnLevel):
    x = np.arange(0, 144, 1)
    occupancy = DataReader.readCsVFile(fileName, columnLevel)

    # print(occupancy)
    plt.plot(x, occupancy)
    plt.legend(['Washing Machine'])
    plt.xlabel('Time (10 minutes)')
    plt.ylabel('Energy Consunption (W)')
    plt.show()