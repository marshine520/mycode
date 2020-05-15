# -*- coding: utf-8 -*-
# coding: utf-8
from subprocess import run, getoutput, Popen
import time
import pandas
import pyexcel
#电视IP，需修改
ip = '192.168.0.101'
#U盘上存放截图的目录(注意：用'\\')，需修改
image_path = r"/mnt/usb/DE40-B39D/png7/"
#image_path1 = r"/mnt/usb/DE40-B39D/png/"
videoIds =r"I:\雷鸟教育\自动化测试\步步高绑定关系导入.xlsx"

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

#file = open(videoIds,'r')
df = pandas.read_excel(videoIds,encoding='gbk')

for videoId,videoName in zip(df['_id'],df['name']):
    run('adb shell am start -a com.tcl.ffeducation.action.cyberui.detail --es videoId '+videoId,
        shell=True)
    print(videoId, videoName)
    time.sleep(8)
    run('adb  shell /system/bin/screencap -p ' + image_path + videoId + '.png', shell=True)
    print("已成功截图")
    time.sleep(8)
    run('adb shell pm clear com.tcl.ffeducation', shell=True)