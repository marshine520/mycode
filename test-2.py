#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools as it
s={1,2,3,4,5,6,7}
Sum=[]
for i in range(0,8):
    a=it.combinations(s,i)
    for x in a:
      tmp=s-set(x)
      for j in range(0,8-i):
          b=it.combinations(tmp,j)
          for y in b:
              z=tmp-set(y)
              Sum.append([set(x),set(y),z])
              print(set(x),set(y),z)      
print(len(Sum))
