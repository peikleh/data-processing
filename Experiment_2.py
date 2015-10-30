
from time import sleep
import serial
import time

import numpy as np
import pylab as plt
import time
import serial
class TestGraph(object):
    def __init__(self):
       # ser = serial.Serial('/dev/ttyACM1', 9600) # Establish the connection on a specific port
         # Establish the connection on a specific port
        self.text_file = open("data.txt", "a")
        self.x=0
        self.y=0 

        self.fig=plt.figure(1)
        self.ax=self.fig.add_subplot(111)
        self.ax.set_xlim(0,5000)
        self.ax.set_ylim(0,5000)


        self.line,=self.ax.plot(self.x,self.y,'ko-')
        #self.loop()
        #sleep(1)

    def serialStart(self):
        count = 0
        c2 = 0
        c3 = 0
        start_time = time.clock()
        while(c3 < 5000):

            
            ser = serial.Serial('/dev/ttyACM0', 9600)
           
            if c2 <= 0:
                start_time = time.clock()
                c2 += 1
            i = ser.readline()
            j = int(i)
            c3 = j
            k = float(time.clock())
            k = k*1000
            if float(time.clock())-float(start_time) <= 5.0 :
                self.text_file.write("%f,%f\n" %(j, time.clock()))
                #print "%d,%f\n" %(j, k)
                self.start(k, j)
            else:
                count += 1
                
        print ""
        print""
        print""
        print "the number of data points in the queue is:"
        print count


    def start(self, x, y):
        self.x = np.concatenate((self.line.get_xdata(),[x]))
        self.y = np.concatenate((self.line.get_ydata(),[y]))
        self.line.set_data(self.x,self.y)
        plt.pause(.01)
        

    def loopTXT(self):
        start = time.clock()
        for i in range(0, 50):
            self.text_file.write('1234\n')
            self.text_file.write('2234\n')
            self.start(i)
        end = time.clock()-start
        
        return end

    def loopCSV(self):
        start = time.clock()
        for i in range(0, 50):
            self.text_file.write('1234,' + '1235\n')
            
            self.start(i)
        end = time.clock()-start
        
        return end


a = TestGraph()
a.serialStart()

"""a = TestGraph()

b = a.loopTXT()
c = a.loopTXT()
d = a.loopTXT()

print ''
print ''
print "Three results for 50 data points txt"
print b
print c
print d
print "Results for txt file"
b = (b + c + d)/150
print b

print ''
print "Three results for 50 data points csv"
b = a.loopCSV()
c = a.loopCSV()
d = a.loopCSV()
print b
print c
print d
print "Results for csv file"
b = (b + c + d)/150
print b"""