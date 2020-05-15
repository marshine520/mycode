#!/usr/bin/python
# -*- coding: utf-8 -*-

name_file = r"C:\Users\yongxin.ma\Desktop\vodlog\test.txt"

aset=set()

for line in open(name_file):
    line=line.strip()
    #ji=line.split("-")[1]
    #print(ji)
    #aset.add(ji)
    aset.add(line)
y=range(len(aset))
for n,x in zip(y,aset):
    print(n+1,x)
    #print(x)