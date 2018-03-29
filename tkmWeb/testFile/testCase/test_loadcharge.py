#出借管理暂时不写
import unittest
from selenium import  webdriver
from testFile.Homepage import basepage
import time
from selenium.common.exceptions import NoSuchElementException


class loadcharge(unittest.TestCase):
    def setUp(self):
        self.driver = basepage.login().succlogin()
        #点击出借管理
        self.driver.find_element_by_xpath('//*[@id="lcgl_"]/li').click()
        time.sleep(2)
    #回款中的债权
    def test_reload(self):
        self.driver.find_element_by_xpath('//*[@id="tab-title-a"]/li[1]').click()
        #滚动到页面底部
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #获取页面总数





