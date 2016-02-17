import csv
import math 
from sklearn.ensemble import RandomForestClassifier 
import time
import numpy as np
import matplotlib.pyplot as plt

start_time = time.clock()
print("--- %s seconds ---" % (time.clock() - start_time))
k = 1

result_upload = []
result = []
data = []
test = []
test_y = []
with open('Sber_test.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
      for elem in row:
          if elem!="":
              print("--- %s seconds ---" % (time.clock() - start_time))
              result_upload.append(float(elem))
#print(result_upload[1])
print("--- %s seconds ---" % (time.clock() - start_time))
window_len = 3
i = 0
sum = 0
sum_arr = []
test_data = []
y = []
while i < len(result_upload):
    if i > window_len - 1:
        start = i -  window_len
        end = i
        for j1 in range(start,end):
            if result_upload[i] > result_upload[j1]:
                sum += 1
            if result_upload[i] < result_upload[j1]:
                sum -= 1 
        sum_arr.append(sum)
    sum = 0
    i += 1
print("--- %s seconds ---" % (time.clock() - start_time))
m = 0
i = 0
sko = []
skval = 0
sk_arr = []
m_arr = []
while i < len(result_upload):
    if i > window_len - 1:
        m = 0
        for j2 in range(0,i):
            m = m + result_upload[j2]
            print(result_upload[j2])
        print (i, m)
        m = m/(i)
        print m
        for j3 in range(0,i):
            sko.append(pow(m - result_upload[j3], 2))
        skval = 0
        for elem1 in sko:
            skval += elem1
        skval = math.sqrt(skval/i)
        print skval
        sk_arr.append(skval)
        sk_arr.append(m)
    i += 1
#print(sk_arr)
#print(len(sk_arr))
#print(len(sum_arr))
#print(len(result_upload))
print("--- %s seconds ---" % (time.clock() - start_time))
while i < len(result_upload) - window_len:
    choice = 0
    if sum > 0 and result_upload[i+window_len] > m_arr[i]:
        y.append(1)
        choice = 1
    if sum < 0 and result_upload[i+window_len] < m_arr[i]:
        y.append(-1)
        choice = 1
    if choice == 0:
        y.append(0)
    i += 1

i = 0
while i < len(result_upload) - window_len:
    print(i)
    test_data.append([result_upload[i+window_len], sum_arr[i], sk_arr[i], m_arr[i]])
    i += 1
    
#y[len(result_upload)-11] = 2
print(test_data)
print(y)
leng = len(result_upload)
leng1 = len(test_data)
print(len(result_upload))
print(len(test_data))

test_len = 2*(len(test_data)/3)
print test_len
i = 0
while i < len(test_data):
    if i < test_len:
        test.append(test_data[i])
        test_y.append(y[i])
    else:
        data.append(test_data[i])
    i += 1
#print test
#print data

forest = RandomForestClassifier(n_estimators = 10)
print("--- %s seconds ---" % (time.clock() - start_time))
forest = forest.fit(test,test_y) 
print("--- %s seconds ---" % (time.clock() - start_time))
output = forest.predict(data)
i = 0
error = 0
while i < len(output):
    if output[i] != y[test_len+i]:
        print(i)
        print(y[test_len+i])
        print(output[i])
        error += 1
    i += 1

print error    
print("--- %s seconds ---" % (time.clock() - start_time))
print(output)