import csv

import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0, 1439, 1)
counter = 0
dataTotal = []
data2 = []

filePath = "C:\\Users\\ngpbh\\Dropbox\\Conducted Data\\Each appliance energy consumption\\Kettle\\weekend\\Winter\\"

allWeekendFiles = os.listdir(filePath)

fileurl = filePath + 'on-prob-daily.csv'

print("Invetigating ", fileurl, "...")
with open(fileurl, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    next(dataReader)
    counter = 0
    prob_start = 0
    prob_stop_holder = 1
    for data in dataReader:
        if counter == 60:
            dataTotal.append(prob_start)
            counter = 0
            prob_start = 0
            prob_stop_holder = 1
        for i in data:
            prob_start += float(i)*prob_stop_holder
            prob_stop_holder = (1 - float(i))*prob_stop_holder
            counter += 1

total_consumption = dataTotal
plt.plot(x, total_consumption)

plt.plot(x, total_consumption)
plt.legend('Avg_Energy_Consumption')
plt.xlabel('Time (1 seconds)')
plt.ylabel('Energy Consunption (W)')
plt.show()

with open('p-start-daily.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in total_consumption:
        writer.writerow([val])