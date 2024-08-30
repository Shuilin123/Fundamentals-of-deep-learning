# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:00:52 2024

@author: dell
"""
import pandas as pd
import time 
import csv
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier


start_time=time.time();
data1=pd.read_csv('5_3.csv');
data1.drop('time',axis=1,inplace=True)
'''
#定义数据集数量 划分数据集
train_num=int(len(data1)*0.7)
test_num=len(data1)-train_num;
train_sets=data1.iloc[1:train_num+1,:]
test_sets=data1.iloc[train_num+1:len(data1),:]
'''
labels=data1['label']
data1.drop('label',axis=1,inplace=True)
# 划分训练集、测试集
xtrain, xtest, label_train, label_test = train_test_split(data1, labels, test_size=0.3)
"""
随机森林所有超参数
sklearn.ensemble.RandomForestClassifier (n_estimators=100, criterion=’gini’, max_depth=None, min_samples_split=2, min_samples_leaf=1, 
                                         min_weight_fraction_leaf=0.0, max_features=’auto’, max_leaf_nodes=None, min_impurity_decrease=0.0, 
                                         min_impurity_split=None, class_weight=None, random_state=None, bootstrap=True, oob_score=False, 
                                         n_jobs=None, verbose=0, warm_start=False)
"""

# 随机森林
rfc = RandomForestClassifier(class_weight='balanced',random_state=37)   
rfc = rfc.fit(xtrain, label_train)
acc = rfc.score(xtest, label_test);
result=rfc.predict(xtest)
data=[{'分类结果':result},{'标签':label_test},{"准确率":acc}]
data=pd.DataFrame(data)
rows=zip(result,label_test);
print('acc is:%.3f'%(acc));
with open('5_4.csv','w',newline='') as f:
    wr=csv.writer(f)
    for row in rows:
        wr.writerow(row)