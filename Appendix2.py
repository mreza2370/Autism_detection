# This Code Prepares 1 million data
number=100
#prepare x and y 
import random
x_points=[]
y_points=[0 for i in range(100)]
for i in range(1,200,2):
    x_points.append(i)
    
    
# data including different classes    
dataA=[]
dataB=[]
dataC=[]
dataD=[]
dataE=[]

label=[[[1,0,0,0,0] for i in range(number)],[[0,1,0,0,0] for i in range(number)],[[0,0,1,0,0] for i in range(number)],[[0,0,0,1,0] for i in range(number)],[[0,0,0,0,1] for i in range(number)]]

"""
# this code is written to show the non-zero elements in every data
n=0
for y in data2[5]:
    if y!=0:
        n+=1
"""        
"""        
#plot the gausiian noise        
import numpy as np
s = np.random.normal(0, 1, 1000)    
#cold use s instead of x   

x=[]
for i in range(1000):
    x.append(random.gauss(0,1))
x= np.asarray(x)

sigma=1
mu=0
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()
"""

############################################################



"""
#plot every data
import matplotlib.pyplot as plt
for i in range(100):
    plt.figure(i)
    #plt.subplot(i+100)
    plt.plot(x_points,dataA[i],'r*')
    plt.savefig('results/A/ %s.png'%i)

"""
"""
import matplotlib.pyplot as plt
plt.plot(x_points,data_ex[1],'r*')
plt.show()
"""


def classA(y_points):
    y_dtat=y_points.copy()
    num=random.randint(0,19)
    s_num=[]
    selected=[]
    for i in range(num):
        rand=random.randint(0,99)
        while(True):
            if rand not in selected:
                selected.append(rand)
                s_num.append(rand)
                break
            else:
                rand=random.randint(0,99)
    for s in s_num:
        y_dtat[s]=random.gauss(0,1)
    return(y_dtat)
        
def classB(y_points):
    y_dtat=y_points.copy()
    num=random.randint(20,39)
    s_num=[]
    selected=[]
    for i in range(num):
        rand=random.randint(0,99)
        while(True):
            if rand not in selected:
                selected.append(rand)
                s_num.append(rand)
                break
            else:
                rand=random.randint(0,99)
    for s in s_num:
        y_dtat[s]=random.gauss(0,1)
    return y_dtat
        
        
def classC(y_points):
    y_dtat=y_points.copy()
    num=random.randint(40,59)
    s_num=[]
    selected=[]
    for i in range(num):
        rand=random.randint(0,99)
        while(True):
            if rand not in selected:
                selected.append(rand)
                s_num.append(rand)
                break
            else:
                rand=random.randint(0,99)
    for s in s_num:
        y_dtat[s]=random.gauss(0,1)
    return y_dtat
        
def classD(y_points):
    y_dtat=y_points.copy()
    num=random.randint(60,79)
    s_num=[]
    selected=[]
    for i in range(num):
        rand=random.randint(0,99)
        while(True):
            if rand not in selected:
                selected.append(rand)
                s_num.append(rand)
                break
            else:
                rand=random.randint(0,99)
    for s in s_num:
        y_dtat[s]=random.gauss(0,1)
    return y_dtat
        
        
def classE(y_points):
    y_dtat=y_points.copy()
    num=random.randint(80,99)
    s_num=[]
    selected=[]
    for i in range(num):
        rand=random.randint(0,99)
        while(True):
            if rand not in selected:
                selected.append(rand)
                s_num.append(rand)
                break
            else:
                rand=random.randint(0,99)
    for s in s_num:
        y_dtat[s]=random.gauss(0,1)
    return y_dtat
    
    
#Create class
# i shows the number of data in each class

for i in range(number):
    outp=classA(y_points)
    dataA.append(outp)
for i in range(number):
    outp=classB(y_points)
    dataB.append(outp)
for i in range(number):
    outp=classC(y_points)
    dataC.append(outp)
for i in range(number):
    outp=classD(y_points)
    dataD.append(outp)
for i in range(number):
    outp=classE(y_points)
    dataE.append(outp)

data=[dataA,dataB,dataC,dataD,dataE]
