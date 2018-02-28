import unittest
from framework import urlutil,firefoxutil
from pagecontrol.control import login_json_control,login_page_control


class LoginParameter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 实例化login、login_json
        self.login = login_page_control.BasePage()

        self.login_para = login_json_control.LoginJsonControl()

        pass

    def setUp(self):
        self.login.Start(urlutil.URL.JD_LOGIN)

    def tearDown(self):
        self.login.Close()
        pass

    # 参数化登录方法
    def test_user_para(self):
        # 遍历参数化list
        for index in self.login_para.GetJson():
            self.login.LoginTab(index['logintab'])
            self.login.LoginUser(index['loginname'],
                                 index['nloginpwd'],
                                 index['username'],
                                 index['password'])
            self.login.LoginTab(index['loginsubmit'])

            # 断言
            self.login.ClassNameAssert(self,index['expects'],index['msg'])

            #截图
            self.login.GetScreens()

            # 清除
            self.login.Clear(index['loginname'],index['nloginpwd'])


        pass
