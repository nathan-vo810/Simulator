import csv

import numpy
import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0, 1439, 1)
eachMinuteConsumption = []

filePath = "C:\\Users\\ngpbh\\PycharmProjects\\Simulator\\each-appliance-ec\\kettle\\weekend\\Winter\\"

allWeekendFiles = os.listdir(filePath)

for fileName in allWeekendFiles:
    fileurl = filePath + fileName
    print("Invetigating ", fileurl, "...")
    with open(fileurl, newline='') as csvfile:
        outputUrl = fileurl[81:91] + "-1min-interval.csv"
        dataReader = csv.reader(csvfile, delimiter=',')
        next(dataReader)
        counter = 0
        minuteConsumption = 0
        for data in dataReader:
            if counter == 60:
                eachMinuteConsumption.append(minuteConsumption)
                minuteConsumption = 0
                counter = 0
            for i in data:
                minuteConsumption += float(i)
                counter += 1
        print("Creating in 1 min interval: ", fileurl, "...")
        with open(outputUrl, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in eachMinuteConsumption:
                writer.writerow([val])
        eachMinuteConsumption.clear()

# plt.plot([], [], color='w', label='On', linewidth=5)
# plt.plot([], [], color='black', label='Off', linewidth=5)
# plt.stackplot(x, on, off, colors=['w', 'black'])
# plt.legend()
# plt.xlabel('Time (1 seconds)')
# plt.ylabel('Probability')
# plt.show()
# #
# print("AVG RF= ", power_on / counter_power_on)
# print("AVG USE TIME= ", sumAll / hold)
# print("Number of use= ", hold / allWeekendFiles.__len__())

# Assuming res is a flat list
# with open('off-prob-daily.csv', "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in off:
#         writer.writerow([val])
# with open('on-prob-daily.csv', "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in on:
#         writer.writerow([val])
