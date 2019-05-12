# -*- coding: utf-8 -*-
import math


"""
Created on Wed May  8 11:09:03 2019

用户输入一个数字，并计算这个数字的平方根

利用幂运算的方法，直接求取该变量的0.5次幂即是开方结果
通过加载math类，然后调用里面的math函数

@author: Dell
"""

x=float(input("请输入一个数字："));
print("该数字的平方根为%f"%(x**0.5));
print("该数字的平方根为%f"%(math.sqrt(x)));