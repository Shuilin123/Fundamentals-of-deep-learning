# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:40:35 2024

@author: dell
"""
import pandas as pd
data1=pd.read_csv('6_2.csv');
data2=pd.read_excel('../datasets/第三题电力看经济/dsjjs_gsqycz.xlsx')
#将第一行作为字段名
listx=list(data2.iloc[0,:]);
data2.columns=listx;
#以表一的户名和表二的企业名称合并成一个表
data=pd.merge(data1,data2,left_on='企业名称',right_on='企业名称',how='inner');
def pearson(x):
    datay=x.loc[:,['2023年上半年电量','2023年上半年产值（万元）']];
    val=datay.corr();
    return val.iloc[0,1];
data_g=data.groupby('分行业').apply(pearson)
#将索引变成值
data_res=data_g.reset_index()
data_res.columns=['分行业','相关系数']
data_res.to_csv('6_3.csv',index=False)
