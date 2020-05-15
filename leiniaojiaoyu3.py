# -*- coding: utf-8 -*-
# coding: utf-8
#Author:yongxin.ma@tcl.com

from subprocess import run, getoutput, Popen
import time
import pandas
import pyexcel
from pathlib import Path
#电视IP，需修改
ip = '192.168.0.101'
#U盘上存放截图的目录(注意：用'\\')，需修改
#image_path = r"/mnt/usb/0000-0000/png10/"
#image_path = r"/mnt/usb/1A08-3620/png26/"
image_path = r"/mnt/usb/0007-9E4B/png2/"
#image_path = r"I:\\雷鸟教育\\自动化测试\\png10\\"
videoIds = r"I:\雷鸟教育\自动化测试\20200513113353_导入结果_绑定关系导入.xlsx"


#使用adb连接设备
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

#获取U盘中已跑的图片打印，类型为字符串
pngfiles = getoutput('adb -s %s:5555 shell ls %s' %(ip,image_path))   

run('adb -s %s:5555 shell mkdir %s' %(ip,image_path), shell=True)   
run('adb -s %s:5555 shell pm clear com.tcl.ffeducation' %ip, shell=True)

#定义空集合
vid = set()

#使用pandas库读取excel表格内容
df = pandas.read_excel(videoIds,encoding='utf-8')

#遍历所有专辑id
for videoId in df['专辑id']:
    vid.add(videoId)

#使用adb命令调起各个视频播放并截图  
g = 1  
for i in vid:
    df1=df.loc[df['专辑id']==i]  
    for videoId,videoName,n in zip(df1['专辑id'],df1['专辑名称'],range(1,len(df1)+1)):
        print(videoId,videoName,n)
             
        #图片已存在，跳过
        if (pngfiles.find((i.strip() + r'-' + str(n))) != -1):
            print("该视频已截图，直接跳过")
            pass
        else:
            run('adb -s %s:5555 shell am start -a com.tcl.ffeducation.action.launcher.history --es videoId %s --es cmdInfo {"index":%d}' %(ip,videoId,n),
                shell=True)
            time.sleep(5)
            run('adb -s %s:5555 shell /system/bin/screencap -p ' %ip + image_path + i.strip() + r'-' + str(n) + r'.png', shell=True)
            print("已成功截图,目前总共截图为：")
            run('adb -s %s:5555 shell ls -lR %s | find /c ".png"' %(ip,image_path), shell=True)
            time.sleep(5)
            run('adb -s %s:5555 shell pm clear com.tcl.ffeducation' %ip, shell=True)
            g = g+1