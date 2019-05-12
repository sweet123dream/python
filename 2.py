# -*- coding: utf-8 -*-

"""
Created on Wed May  8 09:32:35 2019

@author: Dell

用户输入两个数字，并计算两个数字之和：


"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
input()函数用于获取键盘上的输入，并以字符串的形式返回给变量，可以使用强制类型转化
print()函数总结
字符串和数值、变量类型可以直接输出

格式化输出：类似于C中的 printf

print("两个数字之和为%d"%sum,end = '');  加上end = ''后输出过程可以不用换行
"""


 
num1=float(input("请输入第一个数字："));

num2=float(input("请输入第二个数字："));
sum=num1+num2;

#print("两个数字之和为{}：".format(sum));
print(sum)  ;

print("两个数字之和为%d"%sum,end = '');



print("两个数字之和为%f"%(float(input("请输入第一个数字："))+float(input("请输入第二个数字："))));
