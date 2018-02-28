from framework import firefoxutil,urlutil
from selenium import webdriver

class ShopCart(object):
    def __init__(self):
        self.driver = firefoxutil.StartFirfox()

    def Start(self):
        self.driver.OpenFirefox(urlutil.URL.JD_SHOPCART)

    def Close(self):
        self.driver.CloseFirfox()

    def ClassTab(self,classname):
        self.driver.Click(classname)

    def SwitchIFrame(self,id):
        self.driver.SwitchFrame(id)

    # 输入用户名、密码登录
    def Login(self,loginname,nloginpwd,username,password):
        self.driver.SendKeys(loginname, username)
        self.driver.SendKeys(nloginpwd, password)

    # 获取商品价格
    def Price(self,self1):
        self.driver.driver.switch_to_default_content()
        every_prices = self.driver.FindClassNames("p-sum")
        total_price = self.driver.FindClassname("sumPrice")

        #去掉¥，及\n,截取数字:¥23.40 \n 0.34kg
        p_list = []
        for temp in every_prices:
            every_prices_final = str(temp.text)[1:].split('\n')[0]
            p_list.append(float(every_prices_final))

        # 计算商品总和，然后和jd总和比较
        sums = 0
        for temp in p_list:
            sums += temp

        #获取优惠总金额 去掉¥
        totalRePrice = self.driver.FindClassname("totalRePrice")
        totalRePrice_final = str(totalRePrice.text)[2:]

        total_price_final = str(total_price.text)[1:]
        #比较
        count_sum = sums - float(totalRePrice_final)
        self1.assertEqual('{:.2f}'.format(count_sum),'{:.2f}'.format(total_price_final))


