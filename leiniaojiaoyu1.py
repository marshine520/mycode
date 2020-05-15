from subprocess import run, getoutput, Popen
import time
import pandas
import pyexcel
import glob
from pathlib import Path
#电视IP，需修改
ip = '192.168.0.101'
#U盘上存放截图的目录(注意：用'\\')，需修改
image_path = r"/mnt/usb/B4FE-5315/png/"
#image_path1 = r"/mnt/usb/DE40-B39D/png/"
videoIds =r"I:\雷鸟教育\2期\读书郎_0102.csv"
src = r'I:\雷鸟教育\2期\png'
pngfiles=Path(src).rglob('*.png')
names1 = set()
names2 = set()
i=1

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

df = pandas.read_csv(videoIds)

#for videoId,videoName in zip(df['_id'],df['name']):
    #run('adb shell am start -a com.tcl.ffeducation.action.cyberui.detail --es videoId '+videoId,
        #shell=True)
    #print(videoId, videoName)
    #time.sleep(15)
    #run('adb  shell /system/bin/screencap -p ' + image_path + videoName + '.png', shell=True)
    #print("已成功截图")
    #time.sleep(10)
    #run('adb shell pm clear com.tcl.ffeducation', shell=True)
    
for file in pngfiles:
    name=Path(file).name.split('.')[0]
    names1.add(name)
for x in df['name']:
    names2.add(x) 
names3 = names2 - names1

for y in names3:
    df1=df.loc[df['name']==y]
    #for id in df1['_id']:
        #print(id)
    for videoId,videoName in zip(df1['_id'],df1['name']):
        run('adb shell am start -a com.tcl.ffeducation.action.cyberui.detail --es videoId '+videoId,shell=True)
        print(videoId, videoName)
        time.sleep(10)
        run('adb  shell /system/bin/screencap -p ' + image_path + videoId + '.png', shell=True)
        print("已成功截图")
        time.sleep(8)
        run('adb shell pm clear com.tcl.ffeducation', shell=True)