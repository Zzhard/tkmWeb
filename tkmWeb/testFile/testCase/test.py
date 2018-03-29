#控制浏览器滚动条的滚动

from selenium.webdriver.common.action_chains import ActionChains
from selenium import  webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
#滑动到底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
#滑动到顶部
driver.execute_script("window.scrollTo(0,0)");
time.sleep(5)



