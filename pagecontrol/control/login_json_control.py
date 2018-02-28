import json

class LoginJsonControl(object):
    def __init__(self):

        # 引入json路径，打开文件
        self.filepath = "E:/PycharmProjects/jd-login/pagecontrol/data/json.json"
        self.filename = open(self.filepath,encoding='utf-8')

    def GetJson(self):
        # 解析json
        self.result = json.load(self.filename)
        # 返回list
        return self.result

