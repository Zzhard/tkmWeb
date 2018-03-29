from selenium import  webdriver
from  config import config
from comm import log
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testFile.Homepage import basepage
class testInvestment(unittest.TestCase):
    def setUp(self):
        self.driver = basepage.login().succlogin()
        time.sleep(3)
        self.driver.find_element_by_id('invest').click()
        time.sleep(5)
    #小马优先投资\
    def test_invest_xmyx(self):
        #查看‘小马优先’字体后面的数字
        try:
            element=self.driver.find_element_by_xpath('//*[@id="casetitle1"]/span').text
            print(element)
        except Exception as  e:
            print('没有可以投资的标的')
        else:
            if element!=None:
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div[1]/div[3]').click()
                time.sleep(2)
                #查看项目的可借余额
                el1=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[2]/span').text
                el2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[3]/h2').text
                el3=el2.split('\n')[0]
                print(el3)
                print(type(el3))
                str=','
                if el1 != None and el3!=None:
                    if str in el1 :
                        el1 = el1.replace(',', '')
                    num1 = float(el1)
                    if str in el3:
                        el3 = el3.replace(',', '')
                    num2=float(el3)
                #查看可用余额
                # 判断两个数是否都大于100
                print(num1,num2)
                if num1>100 and num2>100:
                    self.driver.find_element_by_id('investmentAmt').send_keys(100)
                    config.logger.info('出借100')
                else:
                    print('可用余额或可借余额小于100，无正常出借')
                self.driver.find_element_by_id('invest_btn').click()
                time.sleep(2)
                #确认借出按钮
                self.driver.find_element_by_id('js-invest-submit').click()
                #确认借出成功按钮
                time.sleep(2)
                # alert2=self.driver.switch_to_alert()
                # alert2.accept()
                self.driver.find_element_by_id('yes').click()
                time.sleep(2)
                el3 = self.driver.find_element_by_id('moneyMemtTabHead')
                print(el3)
                if el3!=None:
                    config.logger.info('出借成功')
                else:
                    config.logger.info('出借失败')
                    print('出借失败')


    # time.sleep(2)
    # print('haha ')
    #小马有财投资
    def test_invest_xmyc(self):
        try:
            self.driver.find_element_by_id('casetitle2').click()
            element=self.driver.find_element_by_xpath('//*[@id="casetitle2"]/span').text
        except Exception as  e:
            print('没有可以投资的标的')

        else:
            if element!=None:
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="loanTable"]/div[1]/dl/dd[3]/div').click()
                time.sleep(2)
                #查看项目的可借余额
                el1=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[2]/span').text
                el2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]/div[3]/span/h2').text
                el3=el2.split('\n')[0]
                print(el3)
                print(type(el3))
                str=','
                if el1 != None and el3!=None:
                    if str in el1 :
                        el1 = el1.replace(',', '')
                    num1 = float(el1)
                    if str in el3:
                        el3 = el3.replace(',', '')
                    num2=float(el3)
                #查看可用余额
                # 判断两个数是否都大于100
                print(num1,num2)
                if num1>100 and num2>100:
                    self.driver.find_element_by_id('investmentAmt').send_keys(100)
                    config.logger.info('出借100')
                else:
                    config.logger.info('可用余额或可借余额小于100，无正常出借')
                    print('可用余额或可借余额小于100，无正常出借')
                self.driver.find_element_by_id('invest_btn').click()
                time.sleep(2)
                #确认借出按钮
                self.driver.find_element_by_id('js-invest-submit').click()
                #确认借出成功按钮
                time.sleep(2)
                # alert2=self.driver.switch_to_alert()
                # alert2.accept()
                # self.driver.find_element_by_id('yes').click()
                time.sleep(5)
                el3 = self.driver.find_element_by_id('moneyMemtTabHead')
                print(el3)
                if el3!=None:
                    config.logger.info('出借成功')
                else:
                    config.logger.info('出借失败')
                    print('出借失败')
    #小马集市
    def test_invest_xmjs(self):

        # @unittest.skip('skip the case')
        try:
            self.driver.find_element_by_id('casetitle3').click()
            element = self.driver.find_element_by_xpath('//*[@id="casetitle3"]/span').text
        except Exception as  e:
            print('没有可以投资的标的')

        else:
            if element != None:
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="transferTable"]/table/tbody/tr[2]/td[5]/div').click()
                time.sleep(2)
                # 查看项目的可借余额
                el1 = self.driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[2]/div[2]/span').text
                el2 = self.driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[2]/div[3]/h2').text
                el3 = el2.split('\n')[0]
                print(el3)
                print(type(el3))
                str = ','
                if el1 != None and el3 != None:
                    if str in el1:
                        el1 = el1.replace(',', '')
                    num1 = float(el1)
                    if str in el3:
                        el3 = el3.replace(',', '')
                    num2 = float(el3)
                # 查看可用余额
                # 判断两个数是否都大于100
                print(num1, num2)
                if num1 > 100 and num2 > 100:
                    self.driver.find_element_by_id('investmentAmt').send_keys(100)
                    config.logger.info('出借100')
                    #点击购买按钮
                    self.driver.find_element_by_id('buyTransfer').click()
                else:
                    config.logger.info('可用余额或可借余额小于100，无正常出借')
                    print('可用余额或可借余额小于100，无正常出借')
                self.driver.find_element_by_id('yes').click()
                time.sleep(2)
                # 确认借出按钮
                # self.driver.find_element_by_id('js-invest-submit').click()
                # 确认借出成功按钮
                # time.sleep(2)
                # alert2=self.driver.switch_to_alert()
                # alert2.accept()
                # self.driver.find_element_by_id('yes').click()
                # time.sleep(5)
                el3 = self.driver.find_element_by_id('zhzl_')
                # print(el3)
                if el3 != None:
                    print('出借成功')
                    config.logger.info('出借成功')
                else:
                    config.logger.info('出借失败')
                    print('出借失败')
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)





