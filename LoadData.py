import csv
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,86400,1)
y = []

with open('2012-06-01.csv', newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for data in dataReader:
        y.append(float(''.join(data)))

plt.plot(x,y)
plt.xlabel('Time(s)')
plt.ylabel('Energy Consumption(W)')
plt.show()