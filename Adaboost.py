# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:13:50 2024

@author: shuilin
"""
import numpy as np
import math
x=np.arange(0,10);
x=x.reshape(1, -1)
y=np.array([1,1,1,-1,-1,-1,1,1,1,-1]).reshape(1, -1)
#初始化权重
w=[1/len(x.T)]*len(x.T)
w=np.array(w).reshape(1,-1)
t=10000;
def sub_classifier(x,val):
    return np.where(np.greater(x,val),-1,1);
    #return 1 if np.greater(x,val) else -1;
#当前分解点
G=[];
alpha=[]#np.array([0,0,0],dtype='float').reshape(1,-1);
#遍历分类器
def argmain_erro(xx,yy,ww):
    min_val=1e10
    min_erro=1e10
    min_y_=0;
    flag=0;
    for v in np.arange(1,9,0.5):
        y_=sub_classifier(xx,v);
        erro=ww[yy!=y_].sum();
        if min_erro>erro and erro>0:
            min_val=v
            min_erro=erro
            min_y_=y_
            flag=1;
        y_=-y_;
        erro=ww[yy!=y_].sum();
        if min_erro>erro and erro>0:
            min_val=v
            min_erro=erro
            min_y_=y_
            flag=-1;
    return min_val,min_y_,min_erro,flag;
T=10000
old_erro=1e10;
signel_G=[];
for t in range(0,T):
    '''
    #计算误差和
    y_=sub_classifier(x,G);
    if t>1:
        y_=-y_;
    #计算估计错的误差
    erro=w[y!=y_].sum();
    '''
    # 求解最优权重
    g,y_,erro,f=argmain_erro(x,y,w)
    if erro>old_erro or erro>0.5:
        #误差大于0.5 或者误差增加
        break
    G.append(g);
    signel_G.append(f);
    old_erro=erro;
    print("erro is:%0.2f"%(erro))
    alpha_t=1/2*math.log((1-erro)/erro,math.e)
    alpha.append(alpha_t);
    #计算Zm
    Zm=np.sum(w*np.exp(-alpha_t*y*y_))
    w=w*np.exp(-alpha_t*y*y_)/Zm
def f(x,alpha):
    res=[]
    for val in x.T:
        sum_x=np.sum(alpha*signel_G*sub_classifier(val[0],G))
        res.append(np.sign(sum_x))
    return np.array(res,dtype='int').reshape(1,-1)
signel_G=np.array(signel_G).reshape(1,-1);
yy=f(x,alpha)
print("y is {}\n yy is {} \n erro is {}".format(y,yy,np.sum(y-yy)));