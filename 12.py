# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:56:40 2019
求阶乘
@author: Dell
"""

def Get(number):
    if number==1:
        return 1;
    else:
        return number*Get(number-1)
    
n=int(input("输入数字"))
print("{0}的阶乘为{1}".format(n,Get(n)))