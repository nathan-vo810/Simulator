import csv

import numpy
import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0, 1439, 1)

filePath = "C:\\Users\\ngpbh\Desktop\Project\household1\\01_plugs_csv\\01\\04\\"

weekendWinter = "weekend-winter\\"
weekendSummer = "weekend-summer\\"
weekdayWinter = "weekday-winter\\"
weekdaySummer = "weekday-summer\\"

classifySeasonAndDate = [weekdayWinter, weekdaySummer, weekendSummer, weekendWinter]

for seasonAndDate in classifySeasonAndDate:
    print("Selecting: ", seasonAndDate, "...")
    specificFilePath = filePath + seasonAndDate
    allWeekendFiles = os.listdir(specificFilePath)
    outputUrl = seasonAndDate[:14] + "AVG-1min-interval.csv"
    minutelyConsumption = [0]*1440
    for fileName in allWeekendFiles:
        fileurl = filePath + seasonAndDate + fileName
        print("Invetigating: ", fileurl, "...")
        with open(fileurl, newline='') as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',')
            next(dataReader)
            counterFor60Secs = 0
            counterFor1440Minute = 0
            currentConsumption = 0
            for data in dataReader:
                if counterFor60Secs == 60:
                    minutelyConsumption[counterFor1440Minute] += currentConsumption
                    currentConsumption = 0
                    counterFor60Secs = 0
                    counterFor1440Minute += 1
                for i in data:
                    if float(i) > 0: currentConsumption += float(i)
                    counterFor60Secs += 1
        counterFor1440Minute = 0
    minutelyConsumption = [minute/allWeekendFiles.__len__() for minute in minutelyConsumption]
    print("Creating in 1 min interval: ", fileurl, "...")
    with open(outputUrl, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        minutelyConsumption.append(0)
        for val in minutelyConsumption:
            writer.writerow([val])
    minutelyConsumption.clear()


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
