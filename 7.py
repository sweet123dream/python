# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:04:57 2019


@author: Dell
"""

import random


print("随机生成一个 [0,1) 的浮点数 %f"%random.random())

print("随机生成一个 [a,b) 的浮点数%f"%random.uniform(10,20))

print("随机生成一个 [a,b] 的整数 %d"%random.randint(10,20))

print("在生成的<以a为始，每step递增，以b为终>这样的一个整数序列中随机选择一个数%d"%random.randrange(2,10,2))