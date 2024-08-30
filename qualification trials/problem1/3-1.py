# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:57:47 2024

@author: dell
"""
import pandas as pd
dat1=pd.read_csv('../datasets/第一题电动车充电桩分析/dsjjs_cdzfx01.csv');
import chardet

with open('../datasets/第一题电动车充电桩分析/dsjjs_cdzfx02.csv', 'rb') as f:
    result = chardet.detect(f.read())  # 读取一定量的数据进行编码检测

print(result['encoding'])
dat2=pd.read_csv('../datasets/第一题电动车充电桩分析/dsjjs_cdzfx02.csv',encoding='GB2312');
dat3=pd.read_csv('../datasets/第一题电动车充电桩分析/dsjjs_cdzfx03.csv');
datetime3=pd.to_datetime(dat3['ds'],format='%Y%m%d')
# & (dat2['char_type']=='专用') & (datetime3.dt.day_name()=='Sunday')
#table2_no=dat2.loc[dat2['char_type']=='专用','cons_id']
data1=pd.merge(dat1, dat2,left_on='cons_id',right_on='cons_id',how='inner')
data2=pd.merge(data1, dat3,left_on='cons_no',right_on='cons_no',how='inner')
data2['ds']=pd.to_datetime(data2['ds'],format='%Y%m%d')
x=(data2['char_type']=='专用')&(data2['lode_attr_code']==3)
y=(data2['ds'].dt.day_name()=='Wednesday')|(data2['ds'].dt.day_name()=='Sunday') 
data=data2[x&y]
data['res']=data['p_e']/data['run_cap']
datax=data.groupby('cons_no')['res'].apply(sum)
datax=pd.DataFrame(datax)
datax=datax.sort_values('res',ascending=False)
datax.to_csv('3_1.csv')



#计算充电时长
dat3x=dat3.groupby('cons_no')['p_e'].apply(sum).reset_index()
dat1x=dat1.loc[dat1['cons_no'].isin(dat3x['cons_no']),['cons_no','run_cap']];
data_time=dat3x['p_e']/dat1x['run_cap'];
#add_time=pd.merge(ata, right)
# 选出迎峰度假日期内的数据
