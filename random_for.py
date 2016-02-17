import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
import csv

result_upload = []
result = []
data = []
test = []
test_y = []
with open('Sber.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      for elem in row:
          if elem!="":
              result_upload.append(float(elem))
print(len(result_upload))
 
 
 

def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma
 
x = range(0,1000000)
y = [3,5,2,4,9,1,7,5,9,1]
 
yMA = movingaverage(x,3)
print yMA

plt.plot(x[len(x)-len(yMA):],yMA)
plt.plot(x[len(x)-len(yMA):],result_upload[0:len(yMA)])
plt.show()
plt.show()
