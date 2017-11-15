import csv

def readCsVFile(fileName, rowNumber):
    data2 = []
    with open(fileName, newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter='\t')
        for data in dataReader:
            data2.append([float(i) for i in data])

    return [row[rowNumber] for row in data2]