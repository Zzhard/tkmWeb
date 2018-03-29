from  selenium import  webdriver
import time
from  config import config
import unittest
from testFile.Homepage import basepage
from selenium.webdriver.support.ui import Select
from testFile.Utils import utils

class Accoutinfo(unittest.TestCase):

    def setUp(self):
        self.driver = basepage.login().succlogin()
        time.sleep(5)
        #点击账户管理
        self.driver.find_element_by_xpath('//*[@id="zhgl_"]/li').click()
        time.sleep(2)

    # @unittest.skip('skip')
    def test_baseinfo(self):
        #点击修改信息
        self.driver.find_element_by_xpath('//*[@id="basicinfo_content"]/div/div[3]/div[2]/input').click()
        time.sleep(1)
        #学历选择“本科”
        Select(self.driver.find_element_by_xpath('//*[@id="js-submit-form"]/div[1]/dl[7]/dd/select')).select_by_index(4)
        #公司
        self.driver.find_element_by_xpath('//*[@id="js-submit-form"]/div[1]/dl[8]/dd/input').send_keys('太空马')
        #月薪
        self.driver.find_element_by_xpath('//*[@id="js-submit-form"]/div[1]/dl[9]/dd/input').send_keys('1000')
        #户籍
        Select(self.driver.find_element_by_id('province')).select_by_index(3)
        time.sleep(1)
        Select(self.driver.find_element_by_id('city')).select_by_index(2)
        time.sleep(1)
        Select(self.driver.find_element_by_id('district')).select_by_index(2)
        #联系地址
        addele=self.driver.find_element_by_xpath('//*[@id="js-submit-form"]/div[1]/dl[11]/dd/input')
        addele.clear()
        addele.send_keys('北京')
        #婚姻状况
        raiobox=self.driver.find_element_by_xpath('//*[@id="d-b"]')
        ele=raiobox.is_selected()
        if ele==False:
            raiobox.click()
        #房产情况
        raiobox1 = self.driver.find_element_by_xpath('//*[@id="a-b"]')
        ele1 = raiobox.is_selected()
        if ele == False:
            raiobox1.click()
        #车产情况
        raiobox2 = self.driver.find_element_by_xpath('//*[@id="b-a"]')
        ele1 = raiobox2.is_selected()
        if ele == False:
            raiobox2.click()
        #点击提交
        self.driver.find_element_by_xpath('//*[@id="js-submit-form"]/div[1]/dl[15]/dd/input[1]').click()

        time.sleep(2)
        text=self.driver.find_element_by_xpath('//*[@id="basicinfo_content"]/div/div[3]/div[1]/ul[6]/dl[2]/dd').text
        self.assertEquals('北京',text)
        config.logger.info('成功修改基本信息')
    #修改安全信息(修改绑定手机号（其他模块不好修改）)
    # @unittest.skip('skip2')
    def test_saveinfo(self):
        #点击安全信息
        self.driver.find_element_by_id('aqxx').click()
        time.sleep(2)
        #点击信息绑定修改
        self.driver.find_element_by_xpath('//*[@id="basicinfo_content"]/div[2]/dl[2]/dd[5]/a/span').click()
        time.sleep(1)
        #获取浏览器句柄
        handles=self.driver.window_handles
        handle1=self.driver.switch_to_window(handles[1])
        #点击获取旧手机短信验证码
        time.sleep(3)
        self.driver.find_element_by_id('web_smsBtn').click()
        #点击确定
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        ele1=self.driver.find_element_by_id('web_yzm')
        ele1.clear()
        ele1.send_keys('0000')
        #输入新手机号(手机号码的函数可以修改，用过利用util中工具)
        phNum=utils.randomtelphone()
        print(phNum)
        ele2=self.driver.find_element_by_id('mobile2')
        ele2.clear()
        ele2.send_keys(phNum)
        #点击获取新手机验证码
        self.driver.find_element_by_id('web_smsBtn2').click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(1)
        ele3=self.driver.find_element_by_id('web_yzm2')
        ele3.clear()
        ele3.send_keys('0000')
        #点击确认变更
        self.driver.find_element_by_xpath('//*[@id="queren"]/a').click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        time.sleep(8)
        self.driver.find_element_by_id('aqxx').click()
        changeNo=self.driver.find_element_by_xpath('//*[@id="basicinfo_content"]/div[2]/dl[2]/dd[4]').text
        str=changeNo.split("*")[1]
        self.assertIn(str,phNum)
        config.logger.info('安全信息修改成功')
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


