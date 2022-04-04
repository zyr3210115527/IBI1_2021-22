import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/ICBC/Downloads")
covid_data= pd.read_csv("full_data.csv")

covid_data.info()
data=covid_data.describe()
print(data)
#The means of new cases is 194.546773. The SD is 2083.395028.
#The range of total cases is between 0 to 777798

a=covid_data.iloc[9:20,0:3:2]#One of the mark points.
print(a)

b=[]
for c in range(0,len(covid_data),1):
    if covid_data.iloc[c,1]=="Afghanistan":
        b.append(True)
    else:
        b.append(False)
print(covid_data.loc[b,"total_cases"])
#All total cases in Afghanistan.

d=[]
for e in range(0,len(covid_data),1):
    if covid_data.iloc[e,1]=="China":
        d.append(True)
    else:
        d.append(False)
list_a=covid_data.iloc[d,[0,2,3]]
list_b=list_a.iloc[:,0]
list_c=list_a.iloc[:,1]
list_d=list_a.iloc[:,2]
list_e=list_a.iloc[:,[1,2]]
f=np.mean(list_c)
g=np.mean(list_d)
print("The mean new cases in China is "+str(f))
print("The mean new deaths in China is "+str(g))
#The mean of the new cases and deaths in China.

plt.subplot(2,2,1)
plt.boxplot(list_c,showmeans=True,showfliers=False,labels=["new cases"])

plt.subplot(2,2,2)
plt.boxplot(list_d,showmeans=True,showfliers=False,labels=["new deaths"])
plt.show()
#The box plot of the new cases and new deaths in China.

plt.plot(list_b,list_c,label="new cases")
plt.plot(list_b,list_d,label="new deaths")
plt.xticks(list_b.iloc[0:len(list_b):4],rotation=-90)#To make the horizontal axis date clear.
plt.title("the new cases and new deaths in China")
plt.legend(fontsize=15)
plt.xlabel("date")
plt.ylabel("number")          
plt.show()
#The plot of the new cases and ner deaths in China

x=[]
for y in range(len(covid_data)):
    if covid_data.iloc[y,0] == "2020-03-31":
        x.append(True)
    else:
        x.append(False)
list_f=covid_data.iloc[x,[1,4]]
t=[]
for w in range(len(list_f)):
    if int(list_f.iloc[w,1])<=10:
        t.append(True)
    else:
        t.append(False)
list_g=list_f.iloc[t,0]
print(list_g)
#Show the contury which havn't yet been more than 10 total infection (as of 31 March).        
        

        




