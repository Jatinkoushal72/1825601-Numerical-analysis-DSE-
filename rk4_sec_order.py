# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:40:42 2026

@author: Student
"""

###rk4
p = 1
q = 1
r = 1
def func(x,y1,y2):
    return p - q*y2 - r*y1
def rk4(xi,y1_i,y2_i,xf,n):
    h = (xf - xi)/n
    xarr,y1_arr,y2_arr = [],[],[]
    xarr.append(xi)
    y1_arr.append(y1_i)
    y2_arr.append(y2_i)
    for i in range(1,n+1):
        k1_y1 = y2_i
        k1_y2 = func(xi,y1_i,y2_i)
        
        k2_y1 = y2_i + (h/2)*k1_y2
        k2_y2 = func(xi + h/2,y1_i + (h/2)*k1_y1,y2_i + (h/2)*k1_y2)
        
        k3_y1 = y2_i + (h/2)*k2_y2
        k3_y2 = func(xi + h/2,y1_i + (h/2)*k2_y1,y2_i + (h/2)*k2_y2)
        
        k4_y1 = y2_i + h*k3_y2
        k4_y2 = func(xi + h,y1_i + (h)*k3_y1,y2_i + (h)*k3_y2)
        
        xi = xi + h
        y1_i = y1_i + (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1)*(h/6)
        y2_i = y2_i + (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2)*(h/6)
        xarr.append(xi)
        y1_arr.append(y1_i)
        y2_arr.append(y2_i)
    return xarr,y1_arr,y2_arr
xres,y1res,y2res = rk4(0,1,1,1,100)
print("Result1:", y1res[-1])
print("Result1:", y2res[-1])


