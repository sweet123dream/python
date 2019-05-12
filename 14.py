# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:28:56 2019

@author: Dell
"""

# Filename : test.py
# author by : www.runoob.com
 
# 用户输入字符
c = input("请输入一个字符: ")
 
# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
 
 
print( c + " 的ASCII 码为", ord(c))    #将一个字符转换为它的整数值    
print( a , " 对应的字符为", chr(a))    #将一个整数转换为一个字符 

