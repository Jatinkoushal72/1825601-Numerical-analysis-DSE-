# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:58:35 2026

@author: Student
"""

import numpy as np
def func(x,y):
    return np.exp(x)
def rk4(x0,y0,xf,n):
    h = (xf - x0)/n
    xarr,yarr = [],[]
    xarr.append(x0)
    yarr.append(y0)
    for i in range(1,n+1):
        k1 = h*func(x0,y0)
        k2 = h*func(x0 + h/2,y0 + k1/2)
        k3 = h*func(x0 + h/2,y0 + k2/2)
        k4 = h*func(x0 + h,y0 + k3)
        x0 = x0 + h
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6
        xarr.append(x0)
        yarr.append(y0)
    return xarr,yarr
xres,yres = rk4(0,1,1,100)
print("Result:", yres[-1])


