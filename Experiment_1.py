from time import sleep
import serial
import time

import numpy as np
import pylab as plt
import time

class TestGraph(object):
    def __init__(self):
       # ser = serial.Serial('/dev/ttyACM1', 9600) # Establish the connection on a specific port
        self.text_file = open("data.txt", "a")
        self.x=0
        self.y=0 

        self.fig=plt.figure(1)
        self.ax=self.fig.add_subplot(111)
        self.ax.set_xlim(0,150)
        self.ax.set_ylim(0,150)


        self.line,=self.ax.plot(self.x,self.y,'ko-')
        #self.loop()
        #sleep(1)
        
    def start(self, x):
        self.x = np.concatenate((self.line.get_xdata(),[x]))
        self.y = np.concatenate((self.line.get_ydata(),[x]))
        self.line.set_data(self.x,self.y)
        plt.pause(.01)

    def loopTXT(self):
        start = time.clock()
        for i in range(0, 50):
            self.text_file.write('1234\n')
            self.text_file.write('2234\n')
            self.start(i)
        end = time.clock()-start
        print end
        return end

    def loopCSV(self):
        start = time.clock()
        for i in range(0, 50):
            self.text_file.write('1234,' + '1235\n')
            
            self.start(i)
        end = time.clock()-start
        print end
        return end
    
        
a = TestGraph()
b = a.loopTXT()
c = a.loopTXT()
d = a.loopTXT()
b = (b + c + d)/150
print "Results for txt file"
print b

b = a.loopCSV()
c = a.loopCSV()
d = a.loopCSV()
b = (b + c + d)/150
print "Results for CSV file"
print b