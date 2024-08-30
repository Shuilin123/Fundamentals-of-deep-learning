import pandas as pd
import time 
import numpy as np 
start_time=time.time();
data1=pd.read_csv('../datasets/第二题风力发电机故障研判/dsjjs_fdyx.csv');
normal=pd.read_csv('../datasets/第二题风力发电机故障研判/dsjjs_failure.csv');
failure=pd.read_csv('../datasets/第二题风力发电机故障研判/dsjjs_normal.csv');
#将字符转化为日期类型
data1['time']=pd.to_datetime(data1['time']);

normal['startTime']=pd.to_datetime(normal['startTime']);
failure['startTime']=pd.to_datetime(failure['startTime']);
normal['endTime']=pd.to_datetime(normal['endTime']);
failure['endTime']=pd.to_datetime(failure['endTime']);
#xx=data1['time']> data2['startTime'] & data1['time']< data2['endTime']
labels=[]
def check(d,date):
    for i in range(0,len(date)):
        if date.iloc[i,0]<=d<=date.iloc[i,1]:
            return True;
    return False;
nor_index=[];
fail_index=[];
for i in range(0,len(data1)):
    d=data1.iloc[i,0];
    label=''
    if check(d, normal):
        label='normal';
        nor_index.append(i);
    else:
        if check(d, failure):
            label='failure';
            fail_index.append(i);
        else:
            label='invalid';
    labels.append(label);
labels=pd.DataFrame(labels);
nor_index=np.array(nor_index);
fail_index=np.array(fail_index);
data1['label']=labels;
data1.to_csv('5_1.csv',index=False)
np.savez('process_data.npz',array1=nor_index,array2=fail_index)
end_time=time.time();
print("runing time is %.4fs"%(end_time-start_time))
#按照标签分组
def process(x):
    num=len(x);
    return num
datax=data1.groupby('label')['label'].apply(process)
datax=pd.DataFrame(datax)
datax['prob']=datax.iloc[:,0]/len(data1);
#datax.columns=["label","count","prob"]
datax.columns=['count','pro'];
data_res=datax.reset_index()
data_res.columns=['label','count','pro']
data_res.to_csv('5_2.csv',index=False)
