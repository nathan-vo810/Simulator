import csv


class DataWriter:
    def writeCsvFile(content,fileName):
        fileName += '.csv'
        with open(fileName, 'w', newline='') as csvfile:
            dataWriter = csv.writer(csvfile, delimiter='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            dataWriter.writerow(content)