from selenium import webdriver
from config import  config





class Driver:

    def __init__(self):
        # self.log = Log.get_log()
        self.logger = config.logger

        self.browser = webdriver.Chrome()

    def open_browser(self):
        """
        Do something for browser
        :return: browser
        """
        self.logger.info("Open browser")

        # 窗口最大化
        self.browser.maximize_window()

        # 打开地址链接
        url = config.url
        self.browser.get(url)
        return self.browser

    def close_browser(self):
        """
        quit browser
        :return:
        """
        self.browser.quit()
        self.logger.info("Quit browser")

    def get_driver(self):
        """
        get web driver
        :return:
        """
        return self.browser
class login():
    def __init__(self):
        self.driver=Driver().open_browser()
    def succlogin(self):
        self.driver.find_element_by_id('tel').send_keys(config.username)
        self.driver.find_element_by_id('pw').send_keys(config.password1)
        self.driver.find_element_by_xpath('//*[@id="df_login"]/input[2]').click()
        config.logger.info('成功打开首页')
        return self.driver

if __name__ == '__main__':
    login().succlogin()
