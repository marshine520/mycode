#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas
import glob
from pathlib import Path
src = r'I:\雷鸟教育\2期\png'
pngfiles=Path(src).rglob('*.png')
videoIds =r"I:\雷鸟教育\2期\读书郎.csv"
i=1
names1 = set()
names2 = set()

df = pandas.read_csv(videoIds)

for file in pngfiles:
    name=Path(file).name.split('.')[0]
    names1.add(name)
for x in df['name']:
    names2.add(x) 
names3 = names2 - names1
global df1
for y in names3:
    df1=df.loc[df['name']==y]
    for id in df1['_id']:
        print(id)