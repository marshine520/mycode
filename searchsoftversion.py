#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:yongxin.ma@tcl.com
# CreateDate: 2018-12-7

import pandas
import pyexcel

name_file = r"I:\云视听极光\机型.txt"
base_file =r"I:\工作表格\机型版本数_1014.xls"
output = r"I:\云视听极光\机型.xls"

datas = {'机器分支':[["机器型号","系统版本号"]]}

df = pandas.read_excel(base_file, sheet_name="机型版本数")


for line in open(name_file):
        line=line.strip()
        #print(line)
        df1=df.loc[df['机型']==line]
        
        try:  
                print(line,"-->",df1['系统版本号'].iloc[0])
                datas['机器分支'].append([line, df1['系统版本号'].iloc[0]])
        except IndexError:
                print("未找到该机型：",line)
       

pyexcel.save_book_as(bookdict=datas, dest_file_name=output)
