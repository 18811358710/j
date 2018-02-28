import unittest
import HTMLTestRunner
from unit import jd_login,jd_login_parameter,shop,jiekou

suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(jd_login.Jd_Login))

# suit.addTest(unittest.makeSuite(shop.ShopCart))

# suit.addTest(unittest.makeSuite(jd_login_parameter.LoginParameter))

suit.addTest(unittest.makeSuite(jiekou.Runwu_Login))

filename = "E:/PycharmProjects/jd-login/html/runwu.html"
files = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=files,
    title=u"京东登录测试",
    description=u"京东登录测试报告"
)
runner.run(suit)