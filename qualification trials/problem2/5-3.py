# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:19:31 2024

@author: dell
"""
import pandas as pd
import time 
import numpy as np 
start_time=time.time();
data1=pd.read_csv('../datasets/第二题风力发电机故障研判/dsjjs_fdyx.csv');
#将字符转化为日期类型
data1['time']=pd.to_datetime(data1['time']);
with np.load('process_data.npz') as data:
    nor_index=data['array1']
    fail_index=data['array2']
def sample(fail_index,nor_index,data1):
    #获取样本数量
    select_num=2*len(fail_index);
    #将normal_index顺序打乱
    #生成列向量suffle只能处理列向量
    nor_index=nor_index.reshape(-1,1)
    fail_index=fail_index.reshape(-1,1)
    np.random.shuffle(nor_index)
    #选择select_num个样本
    nor_index=nor_index[0:select_num];
    #根据索引选数据
    data_nor=data1.iloc[np.squeeze(nor_index),:];
    #加入标签
    data_nor['label']=1;
    data_fail=data1.iloc[np.squeeze(fail_index),:]
    data_fail['label']=0;
    #加入失败样本
    datasets=pd.concat([data_nor,data_fail])
    #重新打乱样本
    index=np.arange(0, len(data_nor)+len(data_fail));
    np.random.shuffle(index)
    smaple_datasets=datasets.iloc[np.squeeze(index),:];
    return smaple_datasets;
datasets=sample(fail_index,nor_index,data1)
datasets.to_csv('5_3.csv',index=False)
