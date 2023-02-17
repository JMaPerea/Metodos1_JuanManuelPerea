# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:11:21 2023

@author: Juan Manuel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import sympy as sym
import urllib.request
from tqdm import tqdm
from time import sleep

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/EstrellaEspectro.txt'

filename = 'Data/DatosMaximo.txt'

urllib.request.urlretrieve(url, filename)

"""
Ejercicio 1 sección 2.01

"""
def factorial(x):
    a=1
    for i in range(0,x):
        a=a*(x-i)
    x=a
    return x
print('Respuesta 1')
for i in range(1,20):

    print(factorial(i)) 
    
"""    
Ejercicio 1 sección 2.02

"""

data = np.loadtxt(filename)
x=data[:,0]
y=data[:,1]
a=np.r_[True, y[1:] > y[:-1]] & np.r_[y[:-1] > y[1:], True]

mx=np.where(a==True)

y2=[]
x2=[]
for i in mx[0]:
    y2.append(y[i])
    x2.append(x[i])
x2=np.array(x2)
y2=np.array(y2)


plt.plot(x,y)
plt.scatter(x2,y2,color='r')

plt.show()

"""
Ejercicio 1 2.03

"""
def fibona(nt):
    n1,n2=0,1
    count=0
    x,y=[],[]
    while count <= nt:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           y.append(n1)
           x.append(count)
           count += 1
    x=np.array(x)
    y=np.array(y)
    return x,y
def aureo(nt):
    n1=(fibona(nt)[1])
    npl=(fibona(nt+1)[1])
    a=[]
    r=0
    while r<=nt:
        s=npl[r+1]/n1[r]
        a.append(s)
        r+=1
    a=np.array(a)
    return a


plt.plot(fibona(20)[0],fibona(20)[1])
plt.show()
plt.plot(fibona(20)[0],aureo(20))

plt.axhline(((1+np.sqrt(5))/2),color='r')
plt.show()

"""
Ejercicio 1 2.08

"""






