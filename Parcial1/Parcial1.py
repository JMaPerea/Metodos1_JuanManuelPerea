# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:48:49 2023

@author: Juan Manuel
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

x=np.arange(-21,21,1)
posT=np.array((-3,2))
posR=np.array((2,-2))

def tiempo_viaje(x,T=posT,R=posR,n0=1,n1=1.33,c=299792458):
    tx=((n0*np.sqrt(((x-T[0])**2)+T[1]**2))+(n1*np.sqrt(((x-R[0])**2)+R[1]**2)))/c
    return tx

t=tiempo_viaje(x)

plt.plot(x,t)
plt.title('Tiempo')
plt.show()

def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)
dt=Derivative(tiempo_viaje, x)

def Derivative2(f,x,h=1e-6):    
    return (f(x+h)-(2*f(x))+f(x-h))/(h**2)



def GetNewtonRaphson(f,df,xn,itmax = 100, precision=1e-5,tv=tiempo_viaje):
    
    error = 1
    it = 0
    
    while error > precision and it <= itmax:
        
        try:
            
            xn1 = xn - f(tv,xn)/df(tv,xn)
            
            error = np.abs(f(tv,xn)/df(tv,xn))
            
            #print(error)
            
        except ZeroDivisionError:
            
            print('Division por cero')
            
        it += 1
        xn = xn1
    
    if it == itmax:
        False
    else:
        return xn


root=GetNewtonRaphson(Derivative, Derivative2, 1)
               
print('Raiz de la funcion',root)







#print(root)

plt.plot(x,dt)
plt.title('Derivada')
#plt.scatter(x,root)
plt.show()

