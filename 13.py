# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:19:25 2019

@author: Dell
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end='')
    print("\n")