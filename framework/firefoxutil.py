from selenium import webdriver
import unittest
from  selenium  import webdriver
import time
from framework import logger

logger = logger.Logger(logger = "StartFirfox").getlog()
class  StartFirfox(object):

    # 定义类被实例化的时候才会被执行的方法，初始化

    # 打开浏览器
    def OpenFirefox(self,url):
        self.driver = webdriver.Firefox()
        logger.info("starting firefox browser")

        self.driver.maximize_window()
        logger.info("maximize the current window")
        self.driver.get(url)
        logger.info("open the url:%s"%url)
        time.sleep(2)
        logger.info("set time sleep 2 seconds")

    # 关闭浏览器
    def CloseFirfox(self):
        self.driver.quit()
        logger.info("now,quit the browser")

    def Click(self,tab):
        tabr = self.FindClassname(tab)
        tabr.click()
        logger.info("click the login tab")

    # 向输入框输入内容
    def SendKeys(self,tab,text):
        tab = self.Findid(tab)
        tab.send_keys(text)
        logger.info("send %s into the inputbox"%text)

    # 清除输入框
    def ClearKeys(self,widget):
        self.Findid(widget).clear()
        logger.info("now clear the keys of inputbox ")

    def GetTitle(self):
        return  self.driver.title
        logger.info("get the title of current page")

    # 保存图片
    def GetWindowPages(self):
        filepath = "E:/PycharmProjects/jd-login/screenshot/"
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        filename = filepath + rq + '.png'

        self.driver.get_screenshot_as_file(filename)
        logger.info("Had taken screenshot and save to folder : /screenshot")

    # 切换frame
    def SwitchFrame(self,id):
        frame = self.Findid(id)
        self.driver.switch_to_frame(frame)

    # # 封装查找控件方法1
    def Findid(self, id):
        time.sleep(2)
        return  self.driver.find_element_by_id(id)

    # # 封装查找控件方法2
    def FindClassname(self,name):
        time.sleep(2)
        return self.driver.find_element_by_class_name(name)

    # # 封装查找控件方法3
    def FindLinktext(self, text):
        time.sleep(2)
        return self.driver.find_element_by_link_text(text)

    # # 封装查找控件方法4
    def FindXpath(self, xpath):
        time.sleep(2)
        return self.driver.find_element_by_xpath(xpath)

    # # 封装查找控件方法5
    def FindTagname(self, tagname):
        time.sleep(2)
        return self.driver.find_element_by_tag_name(id)

    # # 封装查找控件方法6
    def FindCss(self, css):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(css)

    # # 封装查找控件方法7
    def FindPart(self, partial):
        time.sleep(2)
        return self.driver.find_element_by_partial_link_text(partial)

    # # 封装查找控件方法8
    def FindName(self, name):
        time.sleep(2)
        return self.driver.find_element_by_name(name)

    def FindClassNames(self,name):
        time.sleep(2)
        return self.driver.find_elements_by_class_name(name)