import requests
from pagecontrol.control import runwu_login_control
import unittest

class Runwu_Login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.login = runwu_login_control.Runwu_login_control()
        # self.image = runwu_login_control.Runwu_login_control()

        self.downimage = runwu_login_control.Runwu_login_control()
        pass
    def setUp(self):

        pass
    def tearDown(self):

        pass
    # # def test_login(self):
    #     U"""1.登陆接口测试成功"""
    #     self.login.Login_sucess()
    #     # 断言
    #     self.assertEqual(self.login.GetStatus(),0)
    #     self.assertEqual(self.login.GetUsername(),"runwu")
    #     pass

    # def test_image(self):
    #     U"""2.上传图片接口，测试成功"""
    #     self.image.Send_Image()
    #
    #     self.assertEqual(self.image.Get_Status(),0)
    #     pass

    def test_down_image(self):
        U"""3.下载图片，并保存"""
        self.downimage.Down_Image()
        self.downimage.Ifexit()
        self.assertEqual(self.downimage.Ifexit(),True)