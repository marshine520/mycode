#coding=utf-8
from appium import webdriver
import time
import socket


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.180.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

#time.sleep(10)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#size = driver.get_window_size()
#print(size)
#print(size['width'])
#print(size['height'])

#def swipeUp(driver, t=500, n=1):
    #'''向上滑动屏幕'''
    #l = driver.get_window_size()
    #x1 = l['width'] * 0.5     # x坐标
    #y1 = l['height'] * 0.75   # 起始y坐标
    #y2 = l['height'] * 0.25   # 终点y坐标
    #for i in range(n):
        #driver.swipe(x1, y1, x1, y2, t)
        
#swipeUp(driver,n=1)

#i = 0
#for i in range(1000000):
    #i  = i+1
    #nowTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #time.sleep(3)
    #try:
        #em = driver.find_element_by_id('com.miui.home:id/icon_icon')
        #print (nowTime,'第{}次解锁成功'.format(i))
    #except:
        #try:
            #em1=driver.find_element_by_id('com.android.systemui:id/battery_charging_view')
            #print (nowTime,'第{}次解锁失败'.format(i))
            #pass
        #except:
            #em2=driver.find_element_by_id('com.android.systemui:id/keyguard_pin_back_button')
            #print (nowTime,'第{}次解锁失败'.format(i))
    #driver.lock(2)
    #driver.keyevent(26)
    #time.sleep(3)

    


#def runsensetime():
    
    #driver.start_activity('com.sensetime.faceunlock', '.activity.MainActivity')
    #i = 0
    #for i in range(1000000):
        #nowTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ##print(i)
        #driver.find_element_by_id('com.sensetime.faceunlock:id/verify_btn').click()
        #time.sleep(6)
        #try:
            #em = driver.find_element_by_id('com.sensetime.faceunlock:id/confirm_btn')
            #print (nowTime,'第{}次解锁成功'.format(i+1))
            #em1 = driver.find_element_by_id('com.sensetime.faceunlock:id/debug_msg_tv').text
            #print(em1)
            #em.click()
        
        #except:
            #print (nowTime,'第{}次解锁失败'.format(i+1))
            #em2=driver.find_element_by_id('android:id/message').text
            #print(em2)
            #driver.find_element_by_id('android:id/button1').click()    
            #i  = i+1
            
#runsensetime()
#driver.quit()

