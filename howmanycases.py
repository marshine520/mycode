#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas
import glob
from pathlib import Path
src = r'C:\Users\yongxin.ma\Downloads\3.9VOD自动化优化版\TestCase'
yamlfiles=Path(src).rglob('*.yaml')
cases=0
for file in yamlfiles:
    for line in open(file,encoding="UTF-8"):
        if "case_start" in line:
            cases=cases+1
print(cases)