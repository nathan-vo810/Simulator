import csv

import numpy
import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0, 86399, 1)
counter = 0
data2 = []

filePath = "C:\\Users\\ngpbh\Desktop\Project\household1\\01_plugs_csv\\01\\04\\weekend-winter\\"

allWeekendFiles = os.listdir(filePath)

on = [0] * 86400
off = [0] * 86400  # Refrost - Off
power_on = 0
counter_power_on = 0
isOn = False
sumAll = 0
hold = 0
counter = 0
for fileName in allWeekendFiles:
    fileurl = filePath + fileName
    print("Invetigating ", fileurl, "...")
    with open(fileurl, newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')
        next(dataReader)
        refrost_sum = []
        off_sum = []
        for data in dataReader:
            for i in data:
                float_i = float(i)
                if float_i > 10:
                    if not isOn:
                        isOn = True
                    counter += 1
                    refrost_sum.append(1)
                    off_sum.append(0)
                    power_on += float_i
                    counter_power_on += 1
                else:
                    if isOn is True:
                        isOn = False
                        sumAll += counter
                        counter = 0
                        hold += 1
                    refrost_sum.append(0)
                    off_sum.append(1)
        on = [x + y for x, y in zip(on, refrost_sum)]
        off = [x + y for x, y in zip(off, off_sum)]

on = [x / allWeekendFiles.__len__() for x in on]
off = [x / allWeekendFiles.__len__() for x in off]

plt.plot([], [], color='w', label='On', linewidth=5)
plt.plot([], [], color='black', label='Off', linewidth=5)
plt.stackplot(x, on, off, colors=['w', 'black'])
plt.legend()
plt.xlabel('Time (1 seconds)')
plt.ylabel('Probability')
plt.show()

print("AVG RF= ", power_on / counter_power_on)
print("AVG USE TIME= ", sumAll / hold)
print("Number of use= ", hold / allWeekendFiles.__len__())

# Assuming res is a flat list
with open('off-prob-daily.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in off:
        writer.writerow([val])
with open('on-prob-daily.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in on:
        writer.writerow([val])
