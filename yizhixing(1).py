# -*- coding: utf-8 -*-   
#!/usr/bin/python3

import os
import pandas
import pyexcel

pc =r'C:\Users\sensetime\Desktop\0825\one\score.csv'
phone = r'C:\Users\sensetime\Desktop\0825\one\frr_M_Verify_MimicG2Pruned_Common_3.70.0.model.csv'
output_ = r"C:\Users\sensetime\Desktop\0825\one\one.xls"
datas = {'活体数据一致性统计':[["活体数据路径和名称","服务器端活体分数","手机端活体分数","服务器端减手机端活体分数绝对值"]]}

df1 = pandas.read_csv(pc,encoding='gbk')
df2 = pandas.read_csv(phone,encoding='gbk')

for i,j in zip(df1['filename'].str.split(" "),df1['score']):
    #print(i[0],j)
    #print(os.path.basename(i[0]).replace('.ir',''))
    for x,y in zip(df2['path'],df2['hackerscore']):
    #print(x,y)
    #print(os.path.basename(x).replace('_0.gray16',''),y)
        if os.path.basename(i[0]).replace('.ir','') == os.path.basename(x).replace('_0.gray16',''):
            print(i[0],j,y)
            datas['活体数据一致性统计'].append([i[0],float(j),float(y),abs(float(j)-float(y))])
pyexcel.save_book_as(bookdict=datas, dest_file_name=output_) 
