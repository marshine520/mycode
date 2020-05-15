#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas
import pyexcel

videoIds =r"I:\雷鸟教育\2期\读书郎.csv"

df = pandas.read_csv(videoIds)
name=[]
se=set()
#for videoId,videoName in zip(df['_id'],df['name']):
    #print(videoId,videoName)
i=1
for videoName in df['name']:
    #print(i,videoName)
    #i=i+1
    se.add(videoName)
print(len(se))