# -*- coding: utf-8 -*-  
"""  
Created on Fri Aug 30 08:57:47 2024  
  
@author: dell  
"""  
import pandas as pd    
import chardet    
  
# 读取第一个文件    
dat1 = pd.read_csv('datasets/第一题电动车充电桩分析/dsjjs_cdzfx01.csv')    
  
# 检测第二个文件的编码并读取    
with open('datasets/第一题电动车充电桩分析/dsjjs_cdzfx02.csv', 'rb') as f:    
    result = chardet.detect(f.read())    
encoding = result['encoding']    
dat2 = pd.read_csv('datasets/第一题电动车充电桩分析/dsjjs_cdzfx02.csv', encoding=encoding)    
  
# 读取第三个文件    
dat3 = pd.read_csv('datasets/第一题电动车充电桩分析/dsjjs_cdzfx03.csv')    
  
# 合并数据    
data_merged = pd.merge(dat1, dat2, left_on='cons_id', right_on='cons_id', how='inner')    
data_final = pd.merge(data_merged, dat3, left_on='cons_no', right_on='cons_no', how='inner')    
  
# 转换日期并筛选数据    
data_final['ds'] = pd.to_datetime(data_final['ds'], format='%Y%m%d')    
filtered_data = data_final[data_final['p_e'] >= 0.1]    
  
# 检查充电事件之间的时间差是否大于或等于7天  
def has_gap_of_7_days(group):  
    return (group['ds'].diff().shift(-1) >= pd.Timedelta(days=7)).any()  
  
# 标记有间隔的cons_no  
data_with_gaps = filtered_data.groupby('cons_no').apply(has_gap_of_7_days).reset_index(name='has_gap')  
data_with_gaps = data_with_gaps[data_with_gaps['has_gap']]  # 只保留有间隔的记录  
  
# 如果需要筛选原始数据中的这些cons_no  
final_filtered_data = filtered_data[filtered_data['cons_no'].isin(data_with_gaps['cons_no'])]
final_filtered_data=final_filtered_data['cons_no'].drop_duplicates()
final_filtered_data.to_csv('3_2.csv')