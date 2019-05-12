# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:18:34 2019
交换两个变量,使用中间变量或者直接用x,y = y,x

@author: Dell
"""

a=int(input("请输入变量a："))
b=int(input("请输入变量b："))
'''
c=a;
a=b;
b=c;
'''
b,a=a,b;

print("交换变量后a的值大小{}".format(a))

print("交换变量后b的值大小{}".format(b))