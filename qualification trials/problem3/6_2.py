# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:49:34 2024

@author: dell
"""
import pandas as pd
import numpy as np
data1=pd.read_csv('6_1.csv');
data2=pd.read_excel('../datasets/第三题电力看经济/dsjjs_gsqyfl.xlsx')
#以表一的户名和表二的企业名称合并成一个表
data=pd.merge(data1,data2,left_on='户名',right_on='企业名称',how='inner');
data=data.iloc[:,3:];
datax=data.iloc[:,13:16]
#按照列求和
data1=data[['2022年6月电量','2022年5月电量','2022年4月电量','2022年3月电量','2022年2月电量','2022年1月电量']].sum(axis=1)
datax['2022年上半年电量']=data1;
data1=data[['2023年6月电量','2023年5月电量','2023年4月电量','2023年3月电量','2023年2月电量','2023年1月电量']].sum(axis=1)
datax['2023年上半年电量']=data1;
x=(datax['2023年上半年电量']-datax['2022年上半年电量'])/datax['2022年上半年电量'];
datax['同比增幅']=x.apply(lambda xx: format(xx,'.2%'));
datax['同比陡增抖降']='平稳';
datax.iloc[x>0.3,-1]='陡增';
datax.iloc[x<-0.3,-1]='陡抖降';
datax.to_csv('6_2.csv',index=False)