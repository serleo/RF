raw_input()

import csv
from sklearn.ensemble import RandomForestClassifier 
import time
import numpy as np
import matplotlib.pyplot as plt

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

i = 0
sum = 0
test_data = []
y = []
colors = []
while i < len(result_upload):
    if i > 9:
        start = i - 10
        end = i
        for j in range(start,end):
            if result_upload[i] > result_upload[j]:
                sum += 1
            if result_upload[i] < result_upload[j]:
                sum -= 1
        test_data.append([result_upload[i], sum])
        if sum > 0:
            y.append(1)
            colors.append(0.9)
        if sum == 0:
            y.append(0)
            colors.append(0.5)
        if sum < 0:
            y.append(-1)
            colors.append(0.3)
    sum = 0
    i += 1
    
    
y = []
x1 = np.arange(0, 10, 1);
print(x1)
#plt.scatter(x1, result_upload[0:10], c=colors[0:10], alpha=0.3)
plt.plot(result_upload)


plt.show()