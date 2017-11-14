import csv
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,144,1)
y = np.zeros((144,17))
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list2)
data2 = []
# with open('2012-06-01.csv', newline='') as csvfile:
#     dataReader = csv.reader(csvfile)
#     for data in dataReader:
#         y.append(float("".join(data)))
#
# plt.plot(x,y)
# plt.xlabel('Time(s)')
# plt.ylabel('Energy Consumption(W)')
# plt.show()

with open('TotalConsumption.csv', newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=';')
    next(dataReader)
    for data in dataReader:
        data2.append([float(i) for i in data])
        np.append(y,data2)

occupancy = [row[0] for row in data2]
total_demand = [row[1] for row in data2]
light = [row[2] for row in data2]
refrigerator = [row[3] for row in data2]

plt.plot(x,occupancy)
plt.plot(x,total_demand)
plt.plot(x,light)
plt.plot(x,refrigerator)
plt.legend(['Occupancy', 'Total_demand', 'Light', 'Refrigerator'])
plt.xlabel('Time (10 minutes)')
plt.ylabel('Energy Consunption (W)')
plt.show()
