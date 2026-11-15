# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:18:34 2026

@author: Student
"""

import numpy as np
def func(x,y):
    return np.exp(x)
def rk2(x0,y0,xf,n):
    h = (xf - x0)/n
    xarr,yarr = [],[]
    xarr.append(x0)
    yarr.append(y0)
    for i in range(1,n+1):
        k1 = func(x0,y0)
        k2 = func(x0 + h,y0 + h*k1)
        y0 = y0 + 0.5*h*(k1 + k2)
        x0 = x0 + h
        xarr.append(x0)
        yarr.append(y0)
    return xarr,yarr
xres,yres = rk2(0,1,1,100)
print("Result:", yres[-1])

