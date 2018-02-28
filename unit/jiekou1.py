import requests
from selenium import webdriver
import os

# 登陆
# url = "http://192.168.1.2:8080/runwu-app-admin/login"
# datas = {
#     'userName':'runwu',
#     'password':'runwu'
# }
#
# result = requests.post(url,data=datas).json()
# print(result)
# print(result['data'])

# # 上传图片
# url2 = "http://192.168.1.2:8080/runwu-app-admin/upload-pic"
# file = {'file':open('E:/PycharmProjects/jd-login/screenshot/39.jpg','rb')}
#
# result2 = requests.post(url2,files = file)
# print(result2.json())

# 下载文件

url = "http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg"
image = requests.get(url).content

# with open('demo1.apk', 'wb') as fp:
#     fp.write(image)

files = open("E:/PycharmProjects/jd-login/screenshot/demo.jpg",'wb')
files.write(image)
files.flush()
files.close()
# 判断文件是否存在
ifexits = os.path.exists("E:/PycharmProjects/jd-login/screenshot/demo.jpg")
if ifexits ==True:
    print("文件下载成功")
else:
    print("文件下载失败")