import time, subprocess

from subprocess import run

i=1
run('adb kill-server',shell=True)
run('adb connect 192.168.0.105',shell=True)
run('adb disconnect 192.168.0.100',shell=True)
run('adb shell "screencap -p /sdcard/1.png"',shell=True)
run('adb pull /sdcard/1.png D:\\python\\code\\',shell=True)

#调用windows照片查看器查看截图
subprocess.Popen('rundll32.exe shimgvw.dll,ImageView_Fullscreen '+"D:\\python\\code\\1.png")

while(1):
    #使用os.system()会有dos弹窗
    run('adb shell "screencap -p /sdcard/1.png"',shell=True)
    run('adb pull /sdcard/1.png D:\\python\\code\\',shell=True)
    print("已截图" + str(i) + "次")
    i+=1
