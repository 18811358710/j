import unittest
from framework import urlutil,firefoxutil
from pagecontrol.control import shop_cart_control,login_page_control


class ShopCart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # 实例化shop
        self.shop = shop_cart_control.ShopCart()

        pass

    def setUp(self):
        self.shop.Start()
        pass

    def tearDown(self):
        self.shop.Close()
        pass

    # 购物中心
    def test_shop_cart(self):
        self.shop.ClassTab("login-btn")
        self.shop.SwitchIFrame("dialogIframe")
        self.shop.ClassTab("login-tab-r")
        self.shop.Login("loginname","nloginpwd","18811358710","fu910124")
        self.shop.ClassTab("btn-entry")

        self.shop.Price(self)

        pass