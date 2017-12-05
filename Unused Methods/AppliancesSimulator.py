import csv
import numpy as np
import matplotlib.pyplot as plt

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

#Compute the x and y coordinates for points on a sine curve
x = np.arange(0,3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
#Plot the points using matplotlib
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Sine','Cosine'])
plt.show()