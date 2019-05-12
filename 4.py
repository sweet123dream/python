# -*- coding: utf-8 -*-
import cmath
"""
Created on Wed May  8 11:22:08 2019

二次方程式 ax**2 + bx + c = 0
cmath包里面封装了复杂的复数运算，可以计算更加精确的开方结果


@author: Dell
"""



a=float(input("输入a："));
b=float(input("输入b："));
c=float(input("输入c："));

m=b**2-4*a*c;

st1=(-b+cmath.sqrt(m))/(2*a);
st2=(-b-cmath.sqrt(m))/(2*a)

print("结果为{}和{}".format(st1,st2))

"""

# 导入 cmath(复杂数学运算) 模块
import cmath
 
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
# 计算
d = (b**2) - (4*a*c)
 
# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))

"""