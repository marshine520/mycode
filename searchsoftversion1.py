#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:yongxin.ma@tcl.com
# CreateDate: 2018-12-7

import pandas
import pyexcel

name_file = r"C:\Users\yongxin.ma\Desktop\vodlog\机型.txt"
base_file =r"I:\工作表格\机型版本数_20200310.xls"
output = r"C:\Users\yongxin.ma\Desktop\vodlog\第八批.xls"

datas = {'机器分支':[["机芯","机器型号","系统版本号",]]}

df = pandas.read_excel(base_file, sheet_name="机型版本数")

alist=[]
vlist=set()
for line in open(name_file):
    line=line.strip()
    #print(line)
    alist.append(line)
alist.sort() 
for i in alist:
    df1=df.loc[df['机型']==i]
    try:  
        print(i.split("-")[2],i,df1['系统版本号'].iloc[0])
        #print(df1['系统版本号'].iloc[0].split("-")[1])
        #vlist.add(df1['系统版本号'].iloc[0].split("-")[1])
        datas['机器分支'].append((i.split("-")[2],i,df1['系统版本号'].iloc[0]))
    except IndexError:
        print("未找到该机型：",i)

#for v in vlist:
    #print(v)
    
pyexcel.save_book_as(bookdict=datas, dest_file_name=output)
