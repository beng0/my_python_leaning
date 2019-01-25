#coding=utf-8
import unittest,HTMLTestRunner
from base_1 import *
import datetime

class TestApi(unittest.TestCase):
    
    def test_login_success(self):
        r = login_("13418685311","12345678a")
        self.assertTupleEqual(r,(1, "登录成功！",True))
    
    def test_login_account_error(self):
        r = login_('1323232333','12345678a')
        self.assertTupleEqual(r, (0,'账户名与密码不匹配，请重新输入',False))
    def test_login_password_error(self):
        r = login_('13418685311','1234567a')
        self.assertTupleEqual(r, (0,'账户名与密码不匹配，请重新输入',False))
    def test_login_account_none(self):
        r = login_('','12345678a')
        self.assertTupleEqual(r, (-1,'账号和密码不能为空！',False))
    def test_login_password_none(self):
        r = login_('13418685311','')
        self.assertTupleEqual(r, (-1,'账号和密码不能为空！',False))
    def test_ware_house_success(self):
        t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        r = ware_house('hahhahahha'+t)
        self.assertTupleEqual(r, (1,"操作成功",True))
    def test_ware_house_error(self):
        r = ware_house("cangku0001")
        self.assertTupleEqual(r, (0,"错误：该仓库名称已存在",False))
if __name__ == "__main__":
    suite = unittest.TestSuite()
    
    suite.addTests((TestApi("test_login_success"),
                   TestApi("test_login_account_error"),
                   TestApi("test_login_password_error"),
                   TestApi("test_login_account_none"),
                   TestApi("test_login_password_none"),
                   TestApi("test_ware_house_success"),
                   TestApi("test_ware_house_error"),
                   ))
    file = open("E:/keyword/report5.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=file)
    runner.run(suite)
    file.close()















