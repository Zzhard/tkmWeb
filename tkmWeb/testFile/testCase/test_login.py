from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  config import config
from comm import log
import time
import unittest
from testFile.Homepage import basepage




class Login(unittest.TestCase):

    def setUp(self):
        self.driver=basepage.Driver().open_browser()
        # self.driver.maximize_window()
        # self.driver.get(config.url)
        time.sleep(2)
    # def findlogelement(self,ele_login,ele_username,ele_pass,ele_submit):
    #     # 登录按钮
    #     ele_login=self.driver.find_element_by_xpath('//*[@id="header-username"]/div').click()
    #     ele_username=self.driver.find_element_by_id('tel')
    #     ele_pass=self.driver.find_element_by_id('pw')
    #     ele_submit=self.driver.find_element_by_xpath('//*[@id="df_login"]/input[2]')
    def test_login(self):

        self.driver.find_element_by_xpath('//*[@id="header-username"]/div')
        self.driver.find_element_by_id('tel').send_keys(config.username)
        self.driver.find_element_by_id('pw').send_keys(config.password1)
        self.driver.find_element_by_xpath('//*[@id="df_login"]/input[2]').click()
        time.sleep(2)
        element=self.driver.find_element_by_xpath('//*[@id="header-username"]/div/a[1]/strong').text
        self.assertEquals(config.username,element)
    def test_nousername(self):
        self.driver.find_element_by_xpath('//*[@id="header-username"]/div')
        self.driver.find_element_by_id('tel').send_keys('')
        self.driver.find_element_by_id('pw').send_keys(config.password1)
        self.driver.find_element_by_xpath('//*[@id="df_login"]/input[2]').click()
        time.sleep(2)
        text=self.driver.find_element_by_xpath('//*[@id="df_login"]/dl/span').text
        self.assertEquals('用户名不能为空',text)
    def test_nopassword(self):
        self.driver.find_element_by_xpath('//*[@id="header-username"]/div')
        self.driver.find_element_by_id('tel').send_keys(config.username)
        self.driver.find_element_by_id('pw').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="df_login"]/input[2]').click()
        time.sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="df_login"]/dl/span').text
        self.assertEquals('密码不能为空', text)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Login('test_login'))
    # suit.addTest(Login('test_nopassword'))
    # suit.addTest(Login('test_nopassword'))
    runner = unittest.TextTestRunner()
    runner.run(suit)