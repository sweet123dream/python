# -*- coding: utf-8 -*-

"""
Created on Wed May  8 11:39:14 2019

S=√[p(p-a)(p-b)(p-c)] 
p为一半周长
用海伦公式求取三角形面积

面积不能用开方根求取

@author: Dell
"""

a=float(input("请输入边长a："))
b=float(input("请输入边长b："))
c=float(input("请输入边长c："))

m=(a+b+c)/2
area=(m*(m-a)*(m-b)*(m-c))**0.5

print('三角形面积为 %0.2f' %area)