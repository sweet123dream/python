# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

圆的面积公式为 ：3.14*r*r,公式中 r 为圆的半径。

"""


def plus(list):
    st=1;
    for i in list:
        st=st*i;
    return st;

def add(list):
    sm=1;
    for i in list:
        sm=sm+i;
    return sm;

list1 = [10, 20, 1, 45, 99] 
  
print("最大元素为:", max(list1)) 
print("最大元素为:", min(list1)) 
print("所有元素之积:", plus(list1)) 
print("所有元素之:", add(list1)) 