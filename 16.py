# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:45:24 2019

@author: Dell
"""

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

def count(list,x):
    ct=0
    for i in list:
        if i==x:
            ct+=1;
    return ct

print("统计{}出现的次数为{}".format(6,count(lst,6)))



print("统计{}出现的次数为{}".format(10,lst.count(10)))