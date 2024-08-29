# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:26:59 2024

@author: shuilin
"""
import numpy as np
import sklearn.datasets as datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
x=iris.data
y=iris.target
# 只需要第一类和第二类
#获取y<2所有行 0:2列数据
X=x[y<2,0:2];
y=y[y<2];

#获取class1坐标转化为1列
x_c1=X[y==0,0].reshape(-1,1);
y_c1=X[y==0,1].reshape(-1,1);
#获取class2坐标转化为1列
x_c2=X[y==1,0].reshape(-1,1);
y_c2=X[y==1,1].reshape(-1,1);
#得到输入核输出
X=X.T;
Y=y.reshape(1,-1);

w=np.zeros((2,1));
b=0.0;
alpha=0.0001;
m=len(y)
max_iter=10000
def sigmod(x):
    return 1/(1+np.exp(-z));
def CrossEntroy(y,y_):
    return -(np.dot(y,np.log(y_).T)+np.dot(1-y,np.log(1-y_).T));
for iterx in range(1,max_iter):
    #计算输出
    z=np.dot(w.T,X)+b
    y_=sigmod(z);
    J=CrossEntroy(y, y_);
    #变量梯度 
    dz=y_-y;
    dw=np.dot(X,dz.T)/m;
    db=np.sum(dz,axis=1)/m
    J=J/m;
    w=w-alpha*dw;
    b=b-alpha*db;
    
   
    if iterx% 100 == 0:
        plt.scatter(x_c1,y_c1)
        plt.scatter(x_c2,y_c2)
        tempx = [i for i in range(8)]
        tempy = [(-w[0][0]*i-b)/w[1][0] for i in tempx]

        plt.plot(tempx, tempy, 'r-', lw=5)
        plt.text(4, 1.5, 'Loss=%.4f' % J)
        plt.xlim(3, 8)
        plt.ylim(1, 5)
        #plt.title("Iteration: {}\nw: {:.4f} {:.4f}\n b: {}".format(iterx, w[0][0],w[1][0], b))
        plt.pause(0.5)
        plt.clf()
    
