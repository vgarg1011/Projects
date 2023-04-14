# -*- coding: utf-8 -*-
"""VGargHW5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EWBw2RR-HsKLBJISkSOaFbfoGngw6rkf
"""

#importing all the libraries

from pandas.io.parsers.readers import read_table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#normalizing all the features

df = np.genfromtxt('pima-indians-diabetes.csv', delimiter = ',')

dfn = (np.delete(df, 0, 0)).T

for i in range(9):

  max = np.max(dfn[i])
  min = np.min(dfn[i])

  dfn[i] = (dfn[i] - min) / (max - min)

dfn = dfn.T

x = dfn[:,:8]
y = dfn[:,8]

w = np.random.randint(len(x))
print(x[w])

"""Linear Regression: Sum(-(η*(y^ - yt)*xt))
Logistic Regression: Sum(-(η*(y^ - sigmoid(yt))*xt))
"""

#SGD on Linear Regression

x = dfn[500::,:8]
y = dfn[500::,8]
xtest = dfn[:500,:8:]
ytest = dfn[:500:,8]

print(x.shape)


weights = np.zeros(dfn.shape[1]-1)

def SGD_Linear(x, y, w, alpha, xtest, ytest, threshold = 1e-06) :

  wt = w
  Tsum = 1
  loss = []
  step = []
  sse = []
  #loss.append(0)
  #step.append(0)



  #print(wt)

  for i in range(100000):

    w_old = wt

    ind = np.random.randint(len(x))
    xt = x[ind]
    yt = y[ind]

    Tsum = Tsum + (np.dot(wt, xt)-yt)**2

    if i % 100 == 0 and i != 0: 
      
      z = Tsum / i
      loss.append(z)
      step.append(i)

      prediction = np.dot(xtest, wt)
      prediction = prediction >= .5
      prediction = prediction.astype(int)
      v = sse.append(np.sum((prediction - ytest)**2))
    

    wt = wt - alpha*(np.dot(wt, xt)-yt)*xt


    #if np.abs(wt-w_old).max() < threshold:
      #break

  l2 = np.linalg.norm(wt)

  return wt, loss, step, l2, sse


'''www, loss1, step1 = SGD_Linear(x,y,weights,.8,threshold=1e-06)

print(www)

print(step1)

plt.figure()
plt.plot(step1, loss1)
plt.show()'''

#SGD on Logistic Regression

def SGD_Logistic(x, y, w, alpha, xtest, ytest, threshold = 1e-06) :

  wt = w
  Tsum = 1
  loss = []
  step = []
  sse = []

  def sigmoid(q):

    r = 1 / (1 + np.exp(-q))

    return r

  for i in range(1000000):

    ind = np.random.randint(len(x))
    xt = x[ind]
    yt = y[ind]

    Tsum = Tsum + (np.dot(wt, xt)-yt)**2

    if i % 100 == 0 and i != 0: 
      
      z = Tsum / i
      loss.append(z)
      step.append(i)

      prediction = np.dot(xtest, wt)
      prediction = prediction >= .5
      prediction = prediction.astype(int)
      v = sse.append(np.sum((prediction - ytest)**2))
      

    wt = wt - alpha*(sigmoid(np.dot(wt, xt))-yt)*xt

    #if np.abs(wt) < threshold:
      #break

  l2 = np.linalg.norm(wt)

  return wt, loss, step, l2, sse

#Outputs for C

w1lin, loss1lin, step1lin, l2, sse = SGD_Linear(x,y,weights,.8, xtest, ytest, threshold=1e-06)

plt.figure()
plt.plot(step1lin, loss1lin)
plt.title("Linear .8")
plt.show()
print("The l2 norm is:", l2)
print("SSE array: ",  sse)


w1log, loss1log, step1log, l2, sse = SGD_Logistic(x,y,weights,.8, xtest, ytest, threshold=1e-06)

plt.figure()
plt.plot(step1log, loss1log)
plt.title("Logistic .8")
plt.show()
print("The l2 norm is:", l2)
print("SSE array: ",  sse)


w1lin, loss2lin, step2lin, l2, sse = SGD_Linear(x,y,weights,.001, xtest, ytest, threshold=1e-06)

plt.figure()
plt.plot(step2lin, loss2lin)
plt.title("Linear .001")
plt.show()
print(w1lin)
print("The l2 norm is:", l2)
print("SSE array: ",  sse)

w1lin, loss2log, step2log, l2, sse = SGD_Logistic(x,y,weights,.001,xtest,ytest,threshold=1e-06)

plt.figure()
plt.plot(step2log, loss2log)
plt.title("Logistic .001")
plt.show()
print("The l2 norm is:", l2)
print("SSE array: ",  sse)


w1lin, loss3lin, step3lin, l2, sse = SGD_Linear(x,y,weights,.00001, xtest, ytest, threshold=1e-06)

plt.figure()
plt.plot(step3lin, loss3lin)
plt.title("Linear .00001")
plt.show()
print("The l2 norm is:", l2)
print("SSE array: ",  sse)

w1lin, loss3log, step3log, l2, sse = SGD_Logistic(x,y,weights,.00001, xtest, ytest, threshold=1e-06)

plt.figure()
plt.plot(step3log, loss3log)
plt.title("Logistic .00001")
plt.show()
print("The l2 norm is:", l2)
print("SSE array: ",  sse)

#Question D(i):

ws,_,_,_,_ = SGD_Linear(x,y,weights,.001,xtest,ytest)

print(ws)

"""Question D(ii):

I chose to do a Linear Regression with step size .001 because it seemed to be the best. I got the weights that are seen in the ouput above. For every unit increase in BMI, 2 hour insulin level, or Plasma Glucose Level, the odds of a patient having diabetes increases by a factor of the predictor variable's respective weights.

Reflection:

1. This homework took me about 5 hours to complete
2. The learning activites I completed to partake were understanding class lectures and texbook material to grasp the concepts as well as using internet resources to familiarize myself.
3. The resources I used were numerous websites for SGD equations and walkthroughs so I could implement it in code as well as Python syntax databases. I can provide links I just need to find all of them.
4. Completing this homework enhanced my learning by giving me a real application of how the SGD algorithm in class works with an actual data set and how to implement it in code.
"""