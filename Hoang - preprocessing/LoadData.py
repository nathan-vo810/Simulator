import csv

import numpy
import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0, 1439, 1)
eachMinuteConsumption = []

filePath = "C:\\Users\\ngpbh\\PycharmProjects\\Simulator\\1 min interval\\weekend-winter\\"

allWeekendFiles = os.listdir(filePath)
minuteConsumption = [0]*1439
for fileName in allWeekendFiles:
    fileurl = filePath + fileName
    print("Invetigating ", fileurl, "...")
    with open(fileurl, newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        next(dataReader)
        counter = 0
        for data in dataReader:
            for i in data:
                minuteConsumption[counter] += float(i)
                counter += 1
minuteConsumption = [x/allWeekendFiles.__len__() for x in minuteConsumption]

plt.plot(x, minuteConsumption)
plt.show()
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
with open('weekend-winter-avg-1min-energyconsumption.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in minuteConsumption:
        writer.writerow([val])
# with open('on-prob-daily.csv', "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in on:
#         writer.writerow([val])
