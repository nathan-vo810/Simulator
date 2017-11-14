import csv

class Generator(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # Instance Method
    def greet(self):
        print("Hello, %s" % self.name)


a = Generator('TV')
a.greet()

def TVGenerator(x):
    if x > 0:
        return 1000*x
    elif x < 0:
        return 'Invalid'
    else:
        return 0

def FridgeGenerator(x):
    return 50

occupants = 3

print(TVGenerator(occupants))
print(FridgeGenerator(occupants))

with open('appliances.csv', newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for data in dataReader:
        print(', '.join(data))

with open('output.csv','w',newline='') as csvfile:
    dataWriter = csv.writer(csvfile,delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    dataWriter.writerow(['Hello World'])