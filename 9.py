# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:26:58 2019

以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：

@author: Dell
"""

a=float(input("请输入要判断的数字："))
if a>0:
    print("输入的数字为正数")
elif  a<0:
    print("输入的数字为负数")
else:
    print("输入的数字为0")
    