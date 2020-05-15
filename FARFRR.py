#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-8
# merge_testcase_reports.py
import pandas
import glob
import os
import pyexcel

base_file = r'D:\Python学习\睁闭眼批处理脚本\睁闭眼rgb标准测试集_v1.0_3.txt.txt'
version1 = r'C:\Users\sensetime\Desktop\0829\attr\result'
version2 = r'C:\Users\sensetime\Desktop\0829\attr\result'
datas = {'output':[
    ("Version",	"Eye state v2.7.0", "Eye state v2.7.0",	"Eye state v2.7.0","Eye state v2.7.0"),
    ("Threshold", "FAR", "FRR","FAR", "FRR"),]}
output_ = r"C:\Users\sensetime\Desktop\批处理数据\2.6.0.xls"

base_results = {}
for line in open(base_file):
    if line.strip():
        value, filename = line.split()
        #print(value,'-->',filename)
        if value not in base_results:
            base_results[value] = []
        base_results[value].append(filename)

#print(len(base_results['2']))
#values =(9.5,)
values = (8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0,
          9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, )


all_files1 = glob.glob("{}{}*.xls".format(version1,os.sep))
#print(all_files1)
all_data_frames1 = []
for file_name in all_files1:
    df = pandas.read_excel(file_name, sheet_name="睁闭眼")
    #print(df)
    df = df.loc[:,['识别图片的路径','左眼分数','右眼分数','备注']]
    df['识别图片的路径'] = df['识别图片的路径'].str.replace('/sdcard/ocular_base/','')
    #print(df['识别图片的路径'])
    all_data_frames1.append(df)
df = pandas.concat(all_data_frames1, axis=0, ignore_index=True)

#print(df)
values1 = []
for value in values:
    df1 = df.loc[((df['左眼分数'] >= value) | (df['右眼分数'] >=  value)) & df['识别图片的路径'].isin(base_results['0']) , :]
    #print(df1['识别图片的路径'])
    #print(value, len(df1)/109.0)
    df2 = df.loc[((df['左眼分数'] < value) & (df['右眼分数'] <  value)) & df['识别图片的路径'].isin(base_results['1']) , :]
    #print(df2)  
    #print(df2['识别图片的路径'])
    values1.append((len(df1)/len(base_results['0']), len(df2)/179))
    #print(len(df1)/len(base_results['0']))
    #print(len(df2)/len(base_results['1']))
    
all_files2 = glob.glob("{}{}*.xls".format(version2,os.sep))
all_data_frames2 = []
for file_name in all_files2:
    df = pandas.read_excel(file_name, sheet_name="睁闭眼")
    df = df.loc[:,['识别图片的路径','左眼分数','右眼分数','备注']]
    df['识别图片的路径'] = df['识别图片的路径'].str.replace('/sdcard/ocular_base/','')
    #print(df['识别图片的路径'])
    all_data_frames2.append(df)
df = pandas.concat(all_data_frames2, axis=0, ignore_index=True)

#print(df)
values2 = []
for value in values:
    #df1 = df.loc[((df['左眼分数'] >= value) | (df['右眼分数'] >=  value)) & df['识别图片的路径'].isin(base_results['0']) , :]
    df1 = df.loc[((df['左眼分数'] >= value) | (df['右眼分数'] >=  value) & (df['备注'] != '未检测到人脸')) & df['识别图片的路径'].isin(base_results['0']) , :]
    #print(len(df.loc[x]))
    #print(value, len(df1)/109.0)
    #print(df1['识别图片的路径'])
    #for x in df1['识别图片的路径']:
        #print(x)
    df10 = df.loc[(df['备注'] == '未检测到人脸') & df['识别图片的路径'].isin(base_results['0']) , :]
    #print(df10['识别图片的路径'])
    #for x in df10['识别图片的路径']:
        #print(x)
    df2 = df.loc[((df['左眼分数'] < value) & (df['右眼分数'] <  value) & (df['备注'] != '未检测到人脸')) & df['识别图片的路径'].isin(base_results['1']) , :]
    #print(value, len(df2)/179.0) 
    values2.append((len(df1)/len(base_results['0']), len(df2)/len(base_results['1'])))
    #print(df2['识别图片的路径'])
    #print(len(df1)/len(base_results['0']))
    print(len(df2)/len(base_results['1']))
    #for x in df2['识别图片的路径']:
        #print(x)
    df20 = df.loc[(df['备注'] == '未检测到人脸') & df['识别图片的路径'].isin(base_results['1']) , :]
    #for x in df20['识别图片的路径']:
        #print(x)
    #print(df20['识别图片的路径'])
    #print(len(base_results['0']))
    #print(len(base_results['1']))
i = 0 
for value in values:    
    datas['output'].append(
        (value, *values1[i],*values2[i]))   
    i = i + 1


#pyexcel.save_book_as(bookdict=datas, dest_file_name=output_)     

