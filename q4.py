import pandas as df
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
pd = df.read_csv("CatData.csv")
var1 = len(pd.index)
print(" number of rows before processing : ", var1)
var2 = pd.dropna()
var3 = len(var2.index)
print("number of rows after processing :", var3)
num = int(len(pd)*0.8)
train = pd[:num]
tests = pd[num:]
print(len(pd))
print("training set", len(train))
print("testing set", len(tests))

regrsion = linear_model.LinearRegression()
trainx = np.array(train[['Tail Length (cm)']])
trainy = np.array(train[['Mass (kg)']])
regrsion.fit(trainx, trainy)
coefficients = regrsion.coef_
intercept = regrsion.intercept_
print("slope :", coefficients)
print("intercepts", intercept)
plt.scatter(train['Tail Length (cm)'], train['Mass (kg)'])
plt.plot(trainx, coefficients[0]*trainx+intercept, color="red")
plt.title("scatter plot")
plt.xlabel('Tail Length (cm)')
plt.ylabel('Mass (kg)')
plt.show()
