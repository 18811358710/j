import time
import unittest

from framework import urlutil
from pagecontrol.control import login_page_control


class Jd_Login(unittest.TestCase):
    def setUp(self):

        self.driver = login_page_control.BasePage()
        self.driver.Start(urlutil.URL.JD_LOGIN)

    def tearDown(self):
        self.driver.Close()

    def test_jd_pass(self):
        U"""输入正确的用户名、密码，点击登录，登录成功，跳转首页"""
        self.driver.LoginTab("login-tab-r")
        self.driver.LoginUser("loginname","nloginpwd","18811358710","fu910124")
        self.driver.LoginTab("btn-entry")
        time.sleep(2)
        self.driver.GetScreens()

        # 断言
        # self.driver.ClassNameAssert(self,u"请输入账户名和密码","msg-error")

        self.driver.TitleAssert(self,u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
        pass