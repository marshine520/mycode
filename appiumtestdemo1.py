#coding=utf-8
from appium import webdriver
import time
import socket

from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.180.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

#time.sleep(10)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
print(driver.current_package)
print(driver.current_activity)

#driver.start_activity("com.android.mms",".ui.ConversationList")
#print(driver.current_package)
#print(driver.current_activity)

#driver.close_app()



#driver.install_app(r"E:\搜狗下载\a5d37d5c2a47c6552717f4d46b539fce.apk")

#print(driver.page_source)


driver.background_app(8)
#driver.remove_app("com.tencent.android.qqdownloader")
#driver.quit()
driver.find_element(By.XPATH,"啊打发打发")