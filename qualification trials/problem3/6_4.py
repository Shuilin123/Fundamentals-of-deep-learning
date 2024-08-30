# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:49:34 2024

@author: dell
"""
import pandas as pd
# 引入matplotlib库  
import matplotlib.pyplot as plt 
# 设置matplotlib以支持中文显示  
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体  
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题 

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
#2023年上半年电量总耗电量
sumx=data1.sum();
#行业耗电量
sum_p=datax.groupby('分行业')['2023年上半年电量'].apply(sum);
p=sum_p/sumx
 
p=p.reset_index();
# 电量值（万千瓦时）和占比（%），注意这里电量值仅用于图例显示，饼图直接使用占比  
labels = list(p['分行业']);  
sizes = list(p['2023年上半年电量'])  # 占比，总和应为100  
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  
explode = (0.1, 0.2, 0, 0,0,0,0)  # 只有第一个"行业A"会突出显示  
  
# 电量值（仅用于图例显示）
sum_p=sum_p.reset_index()  
electricity_values = sum_p['2023年上半年电量']
# 创建饼图  
plt.figure(figsize=(8, 8))  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)  
# 添加图例，这里使用电量值来标注  
plt.legend(labels, title="电量值（万千瓦时）", labels=[f"{val}万" for val in electricity_values])  
# 添加图表标题  
plt.title('各行业电量占比')  
# 保存图形为jpg文件  
plt.savefig('6-4.jpg')  
  
# 显示图形（可选，如果你想要直接在屏幕上查看）  
plt.show()