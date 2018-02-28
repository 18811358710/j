from selenium import webdriver
from framework import urlutil
import requests
import os

class Runwu_login_control(object):
    def __init__(self):
        # self.url = urlutil.URL().RUNWU_LOGIN
        # self.imageUrl = urlutil.URL().RUNWU_IMAGE

        self.downimage = urlutil.URL().DOWN_IMAGE

    #登陆接口
    # def Login_sucess(self):
    #     self.datas = {
    #         'userName':'runwu',
    #         'password':'runwu'
    #     }
    #     self.result = requests.post(self.url,data=self.datas).json()
    #     return self.result
    #
    # def GetStatus(self):
    #     return self.result['status']
    # def GetData(self):
    #     return self.result['data']
    #
    # def GetUsername(self):
    #     return self.GetData()['name']
    #
    # def GetId(self):
    #     return self.GetData()['id']

    # 上传图片
    # def Send_Image(self):
    #     self.filepath = os.path.dirname(os.getcwd()) + '/pagecontrol/data/39.jpg'
    #     file = {
    #         'file':open(self.filepath,'rb')
    #     }
    #
    #     self.imageResult = requests.post(self.imageUrl,files = file).json()
    #     return self.imageResult
    #     pass
    #
    # def Get_Status(self):
    #     return self.imageResult['status']
    #
    # def Get_Message(self):
    #     return self.imageResult['message']

    # 下载文件/图片
    def Down_Image(self):
        # 下载图片
        self.image = requests.get(self.downimage).content
        self.filepath = os.path.dirname(os.getcwd()) + '/screenshot/demo.jpg'
        self.files = open(self.filepath,"wb")
        self.files.write(self.image)
        self.files.flush()
        self.files.close()

    def Ifexit(self):
        self.ifexit = os.path.exists(self.filepath)
        return self.ifexit

    # def AssertExit(self):
    #     self.driver.assert



