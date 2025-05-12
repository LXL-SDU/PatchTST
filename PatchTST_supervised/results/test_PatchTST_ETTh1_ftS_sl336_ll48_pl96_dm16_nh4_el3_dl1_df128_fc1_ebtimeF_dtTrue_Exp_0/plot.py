#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :plot.py
# @Time      :2025/5/11 下午8:17
# @Author    :LiXiaolong

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 读取 pred.npy 文件
# try:
# 将数据转换为 DataFrame


# 读取 pred.npy 文
import torch.nn.functional as F
import torch

import matplotlib

# data_pred = np.load('./results/ETTh1_96_24_Autoformer_ETTh1_ftM_sl96_ll48_pl24_dm512_nh8_el2_dl1_df2048_fc1_ebtimeF_dtTrue_Exp_0/pred.npy')
data_pred = np.load('pred.npy')
data_pred = torch.from_numpy(data_pred).permute(0, 2, 1)

plt.figure()
print(data_pred.shape)
#预测OT
plt.plot(data_pred[-1, -1, :])  #由于prediction.shape是[1,24,7]那么batch只有1 索引只能是0或-1 都是代表batch这一维本身,如果是加载np文件就不一样了
print(data_pred[-1, -1, :].shape)
plt.show()
plt.plot(data_pred[0, -1, :])  #没问题
print(data_pred[0, -1, :].shape)
plt.show()
# draw HUFL prediction
plt.plot(data_pred[0, 0, :])  #没问题
print(data_pred[-1, -1, :].shape)
plt.show()
'''
Ground Truth
data_gt = np.load('real_prediction.npy')
data_gt = torch.from_numpy(data_gt).permute(0,2,1)
plt.plot(data_gt[-1,-1,:])#由于prediction.shape是[1,24,7]那么batch只有1 索引只能是0或-1 都是代表batch这一维本身,如果是加载np文件就不一样了
print(data_gt[-1,-1,:].shape)
plt.show()
plt.plot(data_gt[0,-1,:])#没问题
print(data_gt[0,-1,:].shape)
plt.show()
# draw HUFL prediction
plt.plot(data_gt[0,0,:])#没问题
print(data_gt[-1,-1,:].shape)
plt.show()
'''


#预测OT

'''
# 将多维数组转换为一维数组
data = np.load('real_prediction.npy')
print("原始数据形状:", data.shape)
flattened_data = data.flatten()
print("转换后一维数组形状:", flattened_data.shape)
df = pd.DataFrame(flattened_data)
df.to_csv("real_pred.csv", index=False)
'''
