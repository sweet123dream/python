# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:13:50 2019

@author: Dell
"""
'''

def swaplist(lis):
    m=lis[0]
    lis[0]=lis[-1]
    lis[-1]=m
    return lis
    
    
ls=[1,7,8,5,6,2]
print(swaplist(ls))
'''
'''

def countNum(param): 
    result = param[0]/(param[1]+param[2]) 
    print("this count: "+str(result)) 
if __name__=="__main__": 
    countNum([10,2,3]) 
    '''
    
#导入模块
from sklearn.model_selection import train_test_split
from sklearn import datasets
#k近邻函数
from sklearn.neighbors import KNeighborClassifier
iris = datasets.load_iris()
#导入数据和标签
iris_X = iris.data
iris_y = iris.target
#划分为训练集和测试集数据
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
#print(y_train)
#设置knn分类器
knn = KNeighborsClassifier()
#进行训练
knn.fit(X_train,y_train)
#使用训练好的knn进行数据预测
print(knn.predict(X_test))
print(y_test)
