# -*- coding: utf-8 -*-
# coding: utf-8
from subprocess import run, getoutput, Popen
import time
import pandas
import pyexcel
#电视IP，需修改
ip = '192.168.0.101'
#U盘上存放截图的目录(注意：用'\\')，需修改
image_path = r"/mnt/usb/864A-42A5/png5/"
#image_path1 = r"/mnt/usb/DE40-B39D/png/"
videoIds =r"I:\雷鸟教育\自动化测试\书小童 绑定关系导入 (1).xlsx"

print("connecting device, please wait...\n")
run('adb kill-server', shell=True)
run('adb connect ' + ip, shell=True)
devices = getoutput("adb devices")
if (devices.count('5555') != 1):
    print("no device or more than one device,please check!\n")
elif (devices.find("offline") != -1):
    print("device offline, please check!\n")
else:
    print("device online!")

vid = set()
df = pandas.read_excel(videoIds,encoding='utf-8')
#print(df)

for videoId in df['专辑id']:
    vid.add(videoId)
g = 1  
for i in vid:
    df1=df.loc[df['专辑id']==i]  
    for videoId,videoName,n in zip(df1['专辑id'],df1['专辑名称'],range(1,len(df1)+1)):
        print(videoId,videoName,n)
        run('adb shell am start -a com.tcl.ffeducation.action.launcher.history --es videoId %s --es cmdInfo {"index":%d}' %(videoId,n),
            shell=True)
        time.sleep(8)
        run('adb shell /system/bin/screencap -p ' + image_path + i.strip() + r'-' + str(n) + r'.png', shell=True)
        print("已成功截图",g)
        time.sleep(8)
        run('adb shell pm clear com.tcl.ffeducation', shell=True)
        g = g+1