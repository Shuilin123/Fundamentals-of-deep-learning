# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:24:12 2024

@author: dell
"""
import struct
import numpy as np
learn_rate=0.01;
#难点1，数据导入及处理
def get_data():
    with open('exercise_data/train-images.idx3-ubyte', 'rb') as lbpath:   # rb二进制形式
        magic, n = struct.unpack('>II', lbpath.read(8))     # magic number用来标示文件格式用，一次从文件中读取8个字节
        labels = np.fromfile(lbpath, dtype=np.uint8)        # 从二进制数据中构造一个数组，返回数组的类型为uint8

    with open('exercise_data/train-labels.idx1-ubyte', 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))# struct.unpack(fmt,string),len(string)必须等于calcsize(fmt)
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)   # len(labels)=60000，imgaes矩阵包含了所有的图片信息
                                                                                  # 60000行，784列，每行是一张图片
    # print(struct.calcsize('>IIII'))
    
    #获取label矩阵，每行是一个label，使用one-hot编码
    list_labels = np.zeros([60000, 10])
    for index in range(60000):
        list_labels[index][labels[index]] = 1
    return list_labels, images
def parameter_initialization():
    # 60隐藏层数 28*28为输入层
    w1=0.001*np.random.rand(60,28*28);
    w2=0.001*np.random.rand(10,60);
    
    b1=0.001*np.random.rand(60,1);
    b2=0.001*np.random.rand(10,1);
    return w1,w2,b1,b2
#激活函数
def sigmod(x):
    return 1/(1+np.exp(-x))
def relu(x):
    return np.maximum(0,x);
def relu_backward(next_dx,x):
    #在x>0 处有导数 否则就为0 其实就是单位阶跃函数
    return np.where(np.greater(x,0),next_dx,0);
def forword(imgs,labels,w1,b1,w2,b2):
    # w1:60x(28*28)
    z1=np.dot(w1,imgs)+b1
    a1=relu(z1)
    z2=np.dot(w2,a1)+b1;
    a2=sigmod(z2)
    return z1,a1,a2
def backword(imgs,labels,z1,a1,a2,w2,batch_size):
   # imgs:输入,labels：标签,z1:第一层输出,a1：隐藏层输出,a2 ：网络输出
   dz2=labels*(a2-1);
   #10x1 60*1  
   dw2=np.dot(dz2,a1.T)/batch_size;
   db2=np.sum(dz2,axis=1,keepdim=True)/batch_size
   da1=np.dot(w2.T,dz2);
   dz1=relu_backward(da1, z1)
   dw1=np.dot(dz1,imgs.T)/batch_size
   db1=np.sum(dz1,axis=1,keepdims=True)/batch_size
   return dw1,dw2,db1,db2
def setp(w1,b1,w2,b2,dw1,dw2,db1,db2):
    w1=w1-learn_rate*dw1
    w2=w2-learn_rate*dw2
    b1=b1-learn_rate*db1
    b2=b2-learn_rate*db2
    return w1,w2,b1,b2
def fc_network(imgs,labels,w1,b1,w2,b2):
    '''
     定义 输入节点数量为28*28 隐含层分别为60 输出层为10的三层全连接网络
    '''
    #输入为列向量
    imgs=imgs.T;
    labels=labels.T;
    batch_size=20
    for bath in range(int(imgs.shape[-1]/batch_size)):
        #第bath堆
        start=bath*batch_size;
        #获取第i堆数据
        batch_imgs=imgs[:,start:start+batch_size]
        batch_labels=labels[:,start:start+batch_size]
        #正向传播
        z1,a1,a2=forword(batch_imgs, batch_labels, w1, b1, w2, b2)
        loss=-batch_labels*np.log(a2);
        #反向传播
        dw1,dw2,db1,db2=backword(imgs,labels,z1,a1,a2,w2,batch_size)
        #更新梯度
        w1,w2,b1,b2=setp(w1,b1,w2,b2,dw1,dw2,db1,db2)
        if bath%10==0:
           print('第{}个bath的loss为{}'.format(bath,loss.mean()/batch_size))
    return w1,w2,b1,b2
w1,w2,b1,b2=parameter_initialization()
labels, images=get_data()
for i in range(1000):
    w1,w2,b1,b2=fc_network(images,labels,w1,b1,w2,b2)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            