# -*- coding: utf-8 -*-
'''
Created on Wed Aug 28 16:41:34 2024

@author: shuilin

'''

import  numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,2.5,50);
y=14530.28*np.exp(-4.738895*x+0.245754*np.random.randn(len(x)))

'''
线性回归
'''
x=x.reshape(1,-1);
y=y.reshape(1,-1);
w=np.random.rand(1,1);
b=np.random.rand(1,1);
max_iter=9000;
alpha=1e-2;
lamda=0;
losses=[];
for i in range(1,max_iter):
    #计算loss
    y_=np.dot(x.T,w)+b;
    y_=y_.T;
    loss=(0.5*(np.dot((y_-np.log(y)).T,y_-np.log(y)))).mean();
    w=w-(alpha*(x*(y_-np.log(y))).mean()+lamda*w);
    b=b-(alpha*(y_-np.log(y)).mean()+lamda*b);
    if i % 100 == 0:
        print("Iteration: {}\nw: {} b: {} Loss={}".format(i, w[0][0], b[0][0],loss)) 
# 必须是（1,50）
        xx=np.linspace(1,2.5,50).reshape(1,-1);
        yy = [i*w[0][0] + b[0][0] for i in xx]
        yy=np.exp(yy);
        yy=np.array(yy);
        plt.scatter(x, y)
        #plt.plot 要是列向量
        plt.plot(xx.T,yy.T);
        plt.pause(0.5)
        plt.clf();
        losses.append(loss)
