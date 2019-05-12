# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:45:25 2019
判断质数

@author: Dell
"""

num=int(input("请输入数字"))

for i in range(2,num):
    if (num%i)==0:
        print("非质数")
        break
    else:
        print("质数")