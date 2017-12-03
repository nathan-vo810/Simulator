import json
import csv


def loadCsv(filename):
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