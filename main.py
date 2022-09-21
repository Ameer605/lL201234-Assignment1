import pandas as df
import matplotlib.pyplot as plt
import pandas as df
import matplotlib.pyplot as plt
import numpy as np

pd=df.read_csv("StudentMarkSheet.csv")
print(pd.shape)
print(pd.info())
print("Number of rows are:")
var1=len(pd.index)
print(var1)
var2=pd.dropna()
var3=len(var2.index)
print("Number of rows after Dropping")
print(var3)
print(pd.loc[pd['Student name']=='James Walker'])
physics=pd[pd['Exam name']=='Physics']['Marks'].mean()
print("physics",physics)
chemistry=pd[pd['Exam name']=='Chemistry']['Marks'].mean()
print("chemistry",chemistry)
biology=pd[pd['Exam name']=='Biology']['Marks'].mean()
print("biology",biology)
philosophy=pd[pd['Exam name']=='Philosophy']['Marks'].mean()
print("philosophy",philosophy)
math=pd[pd['Exam name']=='Mathematics']['Marks'].mean()
print("Mathematics",math)
sociology=pd[pd['Exam name']=='Sociology']['Marks'].mean()
print("Sociology",sociology)
var1=np.array(["mathematics","physics","chemistry","biology","philosophy","sociology","total"])
var2=np.array([math,physics,chemistry,biology,philosophy,sociology,100])
plt.bar(var1,var2)
plt.title("Average marks")
plt.show()