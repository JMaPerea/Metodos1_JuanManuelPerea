# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:31:29 2023

@author: Juan Manuel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import sympy as sym
import urllib.request

"""
Ejercicio 

"""

x=np.arange(-4,4,0.32)
y=np.arange(-4,4,0.32)
R=2


def potflujo(x,y):
    V=2
    p=V*x*(1-((R**2)/((x**2)+y**2)))
    return p
def derivar(x,y):
    h=0.01
    d=(potflujo(x+h, y)-potflujo(x-h,y))/(2*h)
    return d
vx=[]

vy=[]

pos=[]
for i in x :
    for r in y:
        o=derivar(r, i)
        #print(o)
        print(o)
        vx.append(o)
        
        
for i in y :
    for r in x:
        o=derivar(r, i)
        #print(o)
        vy.append(o)
        


vx=np.array(vx)

vy=np.array(vy)
x,y=np.meshgrid(x,y)
pos=np.array(pos)
print(vx)
fig, ax=plt.subplots()
ax.quiver(x,y,vx,vy)


"""
Ejercicio 

"""

"""
Ejercicio 

"""

"""
Ejercicio 

"""