# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:56:09 2019

@author: Dell
"""

def sum_lifang(n):
    sum=0;
    for i in range(1,n+1):
        sum+=i**3
    return sum

print("{}以内的自然数的立方和为{}".format(5,sum_lifang(5)))
        