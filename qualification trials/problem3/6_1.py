# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:11:44 2024

@author: dell
"""
import pandas as pd
import numpy as np
data1=pd.read_excel('../datasets/第三题电力看经济/dsjjs_gsqydl.xlsx');
#处理空值
data1[data1.isna()]=0;
datax=data1.iloc[:,4:-1]
def preprocess(datax):
    #得到小于0的矩阵
    ind=np.array(datax<0)
    #根据bool矩阵得到目标位置
    point=np.argwhere(ind);
    #按照第二列排序
    pointx=point[np.argsort(point[:,1])];
    for p in pointx:
        if p[0]==31 and p[1]==3:
            pdo=0;
        x1=p[1]-1;
        x2=p[1]+1;
        #已经到左边界
        val=-10000;
        if x1<0:
            #当前移动的位置也为异常值一直移动
            while ind[p[0]][x2]==True and x2<ind.shape[1]:
                x2=x2+1
            val= datax.iloc[p[0],x2]
        else:
            #已经到右边界
            if x2>ind.shape[1]:
                #当前移动的位置也为异常值一直移动
                while ind[p[0]][x1]==True and x1>=0:
                    x1=x1-1
                val= datax.iloc[p[0],x1]
            else:
                #注意算法是左边更新过来的 故左边一种是有值的
                val= datax.iloc[p[0],x1] if ind[p[0]][x2]==True else (datax.iloc[p[0],x1]+datax.iloc[p[0],x2])/2
        datax.iloc[p[0],p[1]]=val;
        ind[p[0]][p[1]]=False
    return datax
#更新矩阵
data1.iloc[:,4:-1]=preprocess(datax);
data1=data1.iloc[:,1:-1];
data1.to_csv('6_1.csv',index=False)

     