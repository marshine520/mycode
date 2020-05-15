'''
================================================================
说明：该文件主要用于截图，可以用于黑屏时切换PID、简单的界面测试
使用：修改电视IP和电脑截图存放目录后，直接使用python运行
作者：黄伟
时间：2019.4.1
================================================================
'''

from subprocess import run, getoutput, Popen

#电视IP，需修改
ip = '10.120.30.131'
#电脑上存放截图的目录(注意：用'\\')，需修改
image_path = "D:\\1.手机log抓取方法\\"

def screencap():
    '''======截图函数======'''
    global ip, image_path
    i=1

    print("connecting device, please wait...\n")    
    run('adb kill-server', shell=True)
    run('adb connect ' + ip, shell=True)
    devices = getoutput("adb devices")
    if(devices.count('5555') != 1):
        print("no device or more than one device,please check!\n")
        return False
    elif(devices.find("offline") != -1):
        print("device offline, please check!\n")
        return False
    else:
        print("device online!")

    run('adb shell "screencap -p /sdcard/screencap.png"', shell=True)
    run('adb pull /sdcard/screencap.png ' + image_path, shell=True)

    #调用windows照片查看器查看截图
    Popen('rundll32.exe shimgvw.dll,ImageView_Fullscreen ' + image_path + 'screencap.png')

    #重复截图，windows照片查看器会自动更新图片
    while(1):
        #使用os.system()会有dos弹窗
        run('adb shell "screencap -p /sdcard/screencap.png"', shell=True)
        run('adb pull /sdcard/screencap.png ' + image_path, shell=True)
        print("已截图" + str(i) + "次")
        i+=1
    return True

screencap()
