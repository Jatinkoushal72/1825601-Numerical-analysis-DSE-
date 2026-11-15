# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:30:27 2026

@author: Student
"""
import numpy as np
def func(x):
    return np.exp(x)
def euler(x0,y0,xf,n):
    h = (xf - x0)/n
    xarr,yarr = [],[]
    xarr.append(x0)
    yarr.append(y0)
    for i in range(1,n+1):
        y0 = y0 + h*func(x0)
        x0 = x0 + h
        xarr.append(x0)
        yarr.append(y0)
    return xarr,yarr
xres,yres = euler(0,1,1,10)
print("Result:", yres[-1])


        