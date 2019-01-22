#coding=utf-8

#导入单元测试模块
import unittest
#导入测试报告的模块
import HTMLTestRunner
from read_excel import *
from sendEmail import *

#新建一个类，这个类需要继承来自于单元测试里面的测试用例这个父类
class testProject(unittest.TestCase):
    #不是一定要有的函数，这个是测试开始的函数
    def setUp(self):
        print "test start"
        
    #需要测试的模块或者流程写在中间
    def test_login(self):
        ele = readExcel("login")
        #接收的ele有可能是None值，有可能有值
        self.assertIsNotNone(ele)
    
    def test_booking(self):
        ele = readExcel("booking")
        #接收的ele有可能是None值，有可能有值
        self.assertIsNotNone(ele)
        
    def test_goods(self):
        ele = readExcel("goods")
        #接收的ele有可能是None值，有可能有值
        self.assertIsNotNone(ele)
    
    #表示测试结束的函数
    def tearDown(self):
        print "test end"
        
#定义一个代码运行的主函数入口
if __name__ == "__main__":
    #新建一个测试套件来存放所有的测试用例
    suite = unittest.TestSuite()
    #将测试用例一个一个的放入袋子中
    suite.addTest(testProject("test_login"))
    suite.addTest(testProject("test_booking"))
    suite.addTest(testProject("test_goods"))
    #定义一个测试报告的文件位置和文件名
    file = open("E:/keyword/report.html","wb")    
    #使用测试报告的模块来运行测试套件
    r = HTMLTestRunner.HTMLTestRunner(stream=file,title=u"我的测试报告",description=u"测试加法函数是否正确")
    r.run(suite)
    #最后关闭测试报告的文件
    file.close()
    sendEmail()
        
        
        