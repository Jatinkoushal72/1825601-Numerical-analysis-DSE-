# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:30:57 2026

@author: Jatin
"""
##Gauss Lagure
import numpy as np
def func(x):
    return (np.exp(x))*(1/(x**2 + 1))

x = np.array([0.322548,1.74576,4.53662,9.39507])
w = np.array([0.603154,0.357419,0.038888,0.000539])

IN = np.sum(w*func(x))

print("Gauss Lagure integration:", IN)

##Gauss Hermite
def func(x):
    return (np.exp(x**2))*(1/(x**2 + 1))

x = np.array([-1.650680,-0.524648,1.650680,0.524648])
w = np.array([0.081313,0.804914,0.081313,0.804914])

IN =0.5*np.sum(w*func(x))

print("Gauss Hermite integration:", IN)

##Simpson 1/3rd
def func(x):
    return (1/(x**2 + 1))

def smp_int(n,a,b):
    if n%2!= 0:
        print("Error: n must be even")
        return None
    h = (b-a)/n
    A = func(a) + func(b)
    Y = 0
    for i in range(1,n,2):
        B = 4*(func(a + i*h))
        Y = Y + B
        
        Z = 0
        for i in range(2,n,2):
            C = 2*(func(a + i*h))
            Z = Z + C
        R = (h/3)*(A+Y+Z)
        return R
n = 10
a,b = 0,100
Result = smp_int(n,a,b)
print("Simpsons 1/3rd:", Result)

