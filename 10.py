# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:35:19 2019

判断闰年
能被4整除，并且不能被100整除  或者  能被400整除

@author: Dell
"""
year=int(input("输入年份："))

if(((year%4==0)and((year%100)!=0))or((year%400)==0)):
    print("闰年")
else:
    print("非闰年")

