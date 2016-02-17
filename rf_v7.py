raw_input()

import csv
import math 
from sklearn.ensemble import RandomForestRegressor
import time
import numpy as np
import matplotlib.pyplot as plt
from numpy import convolve

def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
   # print weights
    sma = np.convolve(values, weights, 'valid')
    return sma
 

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
              result_upload.append(float(elem))
#print(result_upload[1])

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
#print("--- %s seconds ---" % (time.clock() - start_time))

yMA = movingaverage(result_upload,window_len)
print yMA

h_l_arr = []
i=0
while i < len(result_upload):
    if i > window_len-1:
        a = abs((result_upload[i] - ((max(result_upload[i-window_len:i-1]) + min(result_upload[i-window_len:i-1]))/2))/((max(result_upload[i-window_len:i-1]) + min(result_upload[i-window_len:i-1]))/2))
        if a > 0.9:
            h_l_arr.append(a)
        else:
            h_l_arr.append(a)
    i +=1
    
m = 0
i = 0
sko = []
skval = 0
sk_arr = []
m_arr = []
while i < len(result_upload):
    #print(result_upload[j2])
    #print ("i = ",i, m)
    if i > 0:
        mi = m/(i)
        #print ("mi = ",mi,i,skval,sko[i-1])
    if i > window_len - 1:
        sko = 0
        for j3 in range(i - window_len + 1,i):
            sko += pow(mi - result_upload[j3], 2)
            #print(sko,mi,j3, result_upload[j3])
        skval = sko/(i)
        #if i== 1 :
            #print(sko, mi)
        #print(skval,mi,i)
        sk_arr.append(skval)
        m_arr.append(mi)
    m = m + result_upload[i]
    i += 1
#print(sk_arr)
print(len(sk_arr))
print(len(sum_arr))
print(len(result_upload))
#print("--- %s seconds ---" % (time.clock() - start_time))
i = 0;
while i < len(result_upload) - window_len:
    y.append(result_upload[i + window_len] - result_upload[i + window_len - 1])
    i += 1
#print(y)

i = 0
while i < len(result_upload) - window_len:
    #print(i)
    test_data.append([result_upload[i+window_len], sum_arr[i], sk_arr[i], m_arr[i], yMA[i], h_l_arr[i]])
    i += 1
#print("--- %s seconds ---" % (time.clock() - start_time))
#y[len(result_upload)-11] = 2
#print(test_data)
#print(y)
leng = len(result_upload)
leng1 = len(test_data)
#print(len(result_upload))
#print(len(test_data))
#print(len(y))

test_len = 2*(len(test_data)/3)
print test_len
i = 0
while i < len(test_data):
    if i < test_len:
        test.append(test_data[i])
        test_y.append(float(y[i]))
    else:
        data.append(test_data[i])
    i += 1
test1_y  = np.asarray(test_y, dtype=np.float32)
#test  = np.asarray(test, dtype=np.float32)
#test1_y = test1_y.transpose
#print(test_y)   
#print data

for i1 in range(0,10):
    forest = RandomForestRegressor(n_estimators = 100, max_depth = 3)
#print("--- %s seconds ---" % (time.clock() - start_time))
    forest = forest.fit(test,test1_y) 
    out1 = forest.apply(test) 
    out = forest.score(test,test1_y) 
    print out
    print out1
#print("--- %s seconds ---" % (time.clock() - start_time))
    output = forest.predict(data)
    i = 0
    error = 0
    error1 = 0
    while i < len(output):
        if abs(output[i] - y[test_len+i]) > 0.01:
            #print(i)
            #print(y[test_len+i])
            #print(output[i])
            error += abs(output[i] - y[test_len+i])
            error1 += 1
        i += 1

    print("error = ", error, " in ", error1, " of ", len(test_data) - test_len)    
print("--- %s seconds ---" % (time.clock() - start_time))
#print(output)