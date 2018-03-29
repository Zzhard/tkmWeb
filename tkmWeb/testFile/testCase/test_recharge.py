from  selenium import  webdriver
import time
from  config import config
import unittest
from testFile.Homepage import basepage



class testinvest(unittest.TestCase):
    def setUp(self):
        self.driver=basepage.login().succlogin()
        time.sleep(5)
    # 账户总览中充值
    def test_recharge(self):
        #为断言取可用余额中的值
        element1= self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/span').text
        str=','
        if element1!=None:
            if str in element1:
                element1=element1.replace(',','')
            num1=float(element1)
        print(num1)
        time.sleep(2)
        #点击充值
        self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/div[2]/input[1]').click()
        time.sleep(2)
        #选择充值方式并点击
        self.driver.find_element_by_id('js-eb').click()
        self.driver.find_element_by_id('tranAmt').send_keys('100')
        config.logger.info('充值100')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div/dl[6]/input').click()
        time.sleep(3)
        #切换到富有充值页面
        handles1=self.driver.window_handles
        # print(handles)
        time.sleep(2)
        handle1=self.driver.switch_to.window(handles1[1])
        # print(self.driver.current_url)
        time.sleep(2)
        self.driver.find_element_by_css_selector('#b2cDTd>a').click()
        radiobox=self.driver.find_element_by_xpath('//*[@id="08041058400b2cDBusiCtrlListSize"]').click()
        # sel=radiobox[1].is_selected()
        # if sel==False:
        #     radiobox[1].click()
        self.driver.find_element_by_id('subbutton').click()
        time.sleep(10)
        handles2 = self.driver.window_handles
        # print(handles2)
        handle2 = self.driver.switch_to.window(handles2[2])
        # print(self.driver.current_url)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="zhzl_"]/li').click()
        time.sleep(3)
        element2=self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/span').text
        if element2!=None:
            if str in element2:
                element2=element2.replace(',','')
            num2=float(element2)
        self.assertEquals(num2,num1+100)
        config.logger.info('充值成功')
    #账户总览中的提现
    def test_cash(self):
        self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/div[2]/input[2]').click()
        time.sleep(2)
        element=self.driver.find_element_by_id('js-user-money').text
        print(element)
        str=','
        if str in element:
            element=element.replace(',','')
        num=float(element)
        #对提现金额必须大于10不进行判断
        try:
            if num>10:
                num=int(num*0.01)
            config.logger.info('提现%d元'%(num))
            self.driver.find_element_by_id('money').send_keys(num)
            self.driver.find_element_by_xpath('//*[@id="withdraw"]/div/dl[6]/input').click()
            time.sleep(3)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            #确认输入支付密码
            self.driver.find_element_by_id('web500003_password').send_keys('88888888Z')
            # 点击获取短信验证码
            self.driver.find_element_by_xpath('//*[@id="web500003_smsBtn"]').click()
            time.sleep(2)
            #点击弹框的确定
            alert1=self.driver.switch_to_alert()
            time.sleep(3)
            alert1.accept()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="web500003_yzm"]').send_keys('0000')
            self.driver.find_element_by_xpath('//*[@id="queren"]/a').click()
            #对弹框进行确认支付(未完成)
            alert2 = self.driver.switch_to_alert()
            time.sleep(1)
            alert2.accept()
            time.sleep(8)
            config.logger.info('提现成功')
        except Exception as e:
            print('可用金额小于最小可体现金额，不可提现')

    # 资金管理中的账户充值
    def test_capital_recharge(self):
        element1 = self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/span').text
        str = ','
        if element1 != None:
            if str in element1:
                element1 = element1.replace(',', '')
            num1 = float(element1)
        # print(num1)
        time.sleep(3)
        #点击资金管理
        self.driver.find_element_by_xpath('//*[@id="zjgl_"]/li').click()
        time.sleep(3)
        #点击账户充值
        self.driver.find_element_by_id('zhcz').click()
        time.sleep(2)
        self.driver.find_element_by_id('js-eb').click()
        self.driver.find_element_by_id('tranAmt').send_keys('100')
        config.logger.info('充值100')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div/dl[6]/input').click()
        time.sleep(3)
        # 切换到富有充值页面
        handles1 = self.driver.window_handles
        # print(handles)
        time.sleep(2)
        handle1 = self.driver.switch_to.window(handles1[1])
        # print(self.driver.current_url)
        time.sleep(2)
        self.driver.find_element_by_css_selector('#b2cDTd>a').click()
        radiobox = self.driver.find_element_by_xpath('//*[@id="08041058400b2cDBusiCtrlListSize"]').click()
        # sel=radiobox[1].is_selected()
        # if sel==False:
        #     radiobox[1].click()
        self.driver.find_element_by_id('subbutton').click()
        time.sleep(10)
        handles2 = self.driver.window_handles
        # print(handles2)
        handle2 = self.driver.switch_to.window(handles2[2])
        # print(self.driver.current_url)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="zhzl_"]/li').click()
        time.sleep(3)
        element2 = self.driver.find_element_by_xpath('//*[@id="member_content"]/div/div[1]/dl/span').text
        if element2 != None:
            if str in element2:
                element2 = element2.replace(',', '')
            num2 = float(element2)
        self.assertEquals(num2, num1 + 100)
        config.logger.info('充值成功')
    #资金管理中的账户提现
    def test_capital_cash(self):
        self.driver.find_element_by_xpath('//*[@id="zjgl_"]/li').click()
        time.sleep(3)
        self.driver.find_element_by_id('wytx').click()
        time.sleep(2)
        element1=self.driver.find_element_by_id('js-user-money').text
        print(element1)
        str=','
        if str in element1:
            element=element1.replace(',','')
        num=float(element)
        #对提现金额必须大于10不进行判断
        try:
            if num>10:
                num=int(num*0.01)
            config.logger.info('提现%d元'%(num))
            self.driver.find_element_by_id('money').send_keys(num)
            self.driver.find_element_by_xpath('//*[@id="withdraw"]/div/dl[6]/input').click()
            time.sleep(3)
            handles=self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            #确认输入支付密码
            self.driver.find_element_by_id('web500003_password').send_keys('88888888Z')
            # 点击获取短信验证码
            self.driver.find_element_by_xpath('//*[@id="web500003_smsBtn"]').click()
            time.sleep(2)
            #点击弹框的确定
            alert1=self.driver.switch_to_alert()
            time.sleep(3)
            alert1.accept()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="web500003_yzm"]').send_keys('0000')
            self.driver.find_element_by_xpath('//*[@id="queren"]/a').click()
            #对弹框进行确认支付(未完成)
            alert2 = self.driver.switch_to_alert()
            time.sleep(1)
            alert2.accept()
            time.sleep(8)
            config.logger.info('提现成功')
        except Exception as e:
            print('可用金额小于最小可体现金额，不可提现')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)


