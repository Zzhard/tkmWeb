"""
ui定位未能完成，暂时不写
"""

from  appium import  webdriver
import time
from config import config




desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['appPackage']='com.taikongma'
desired_caps['appActivity']='com.taikongma.IndexActivity'
#输入中文需要设置的两个参数
desired_caps['resetKeyboard']='True'
desired_caps['unicodeKeyboard']='True'


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(2)
classnames=driver.find_element_by_class_name('android.widget.TextView').click()

