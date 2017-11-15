import csv


class DataWriter:
    def writeCsvFile(content):
        with open('output.csv', 'w', newline='') as csvfile:
            dataWriter = csv.writer(csvfile, delimiter='\n', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            dataWriter.writerow(content)