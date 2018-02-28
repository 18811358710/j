import unittest
import time
from selenium import webdriver
from framework import logger,firefoxutil
from pagecontrol.control import login_json_control

logger = logger.Logger(logger = "BasePage").getlog()
class BasePage(object):
    def __init__(self):

        # 实例化浏览器
        self.driver = firefoxutil.StartFirfox()

    def Start(self,url):
        self.driver.OpenFirefox(url)

    def Close(self):
        self.driver.CloseFirfox()

    # 截屏保存
    def GetScreens(self):
        self.driver.GetWindowPages()

    # 切换账户登录、点击登录
    def LoginTab(self,classname):
        self.driver.Click(classname)

    # 输入用户名、密码
    def LoginUser(self,loginname,nloginpwd,username,password):
        self.driver.SendKeys(loginname,username)
        self.driver.SendKeys(nloginpwd,password)

    # 清除输入框内容
    def Clear(self,widget1,widget2):
        self.driver.ClearKeys(widget1)
        self.driver.ClearKeys(widget2)

    # msg-error断言
    def ClassNameAssert(self,self1,excepts,classname):
        message = self.driver.FindClassname(classname).text
        self1.assertEqual(message,excepts)
        logger.info("add the assert of %s"%excepts)

    # title断言
    def TitleAssert(self,self1,excepts):
        title = self.driver.GetTitle()
        self1.assertEqual(title,excepts)
        logger.info("add the assert of %s"%excepts)





