#coding=utf-8

#导入在自动化过程中可能用到的所有模块
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time,SendKeys
import random

#定义一个浏览器操作的类，这个类中全部都是和浏览器操作相关的方法
class Browser_():
    #定义一个浏览器的构造函数
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    #因为每个操作都需要定位元素，所以单独写上一个定位元素的方法
    #1.智能等待获取元素 2.使用时间格式来保存截图
    def get_position(self,position):
        driver = self.driver
        
        #使用=号来切割位置的字符串
        position = position.split("=")
        #将列表的第一个位置保存的定位方法给到一个变量保存起来
        method = position[0]
        #因为方法保存给了method，所以可以将它从列表中删除掉
        position.pop(0)
        #将剩余的所有值，用=号重新连接起来
        value = "=".join(position)
        
        try:
            if method == "id":
                ele = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_id(value))
            elif method == "name":
                ele = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_name(value))
            elif method == "class":
                ele = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_class_name(value))
            elif method == "xpath":
                ele = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath(value))
            elif method == "css":
                ele = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_css_selector(value))
            else:
                print "暂时没有这个方法，请联系系统管理员"
        except Exception:
            #如果元素没有找到，能够自动的捕获当前浏览器的截图
            import datetime
            t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            driver.get_screenshot_as_file("C:/screen/%s.jpg"%t)
            #没有找到的时候，给调用的人返回一个空值
            return None
        else:
            #找到了就返回正确的元素位置
            return ele
        
    #如果关键字是open，那么我们就需要定义一个浏览器打开的操作方法
    def open_(self,data,time=10):
        self.driver.get(data)
        self.driver.implicitly_wait(time)
    
    #如果关键字是click，那么就需要定义一个点击元素的操作方法
    def click_(self,position):
        #通过自己编写的定位方法，来获取元素的具体位置
        ele = self.get_position(position)
        if ele!=None:
            ele.click()
        else:
            print "要点击的元素没有找到！"
    
    def input_(self,position,data):
        ele = self.get_position(position)
        if ele!=None:
            ele.clear()
            ele.send_keys(data)
        else:
            print "输入框没有找到！"     
    
    #如果要运行js脚本语句，那么需要定义一个专门操作js代码的方法
    def js_(self,data):
        self.driver.execute_script(data)
        
    #要上传文件，定义和上传文件操作相关的方法
    def upload_(self,data,position):
        ele = self.get_position(position)
        if ele!=None:
            ele.click()
            time.sleep(2)
            #因为上传文件的字符串一定不能是unicode编码，所以需要先转码才能用
            data = data.encode("utf8")
            SendKeys.SendKeys(data)
            SendKeys.SendKeys("{ENTER}")
        else:
            print "上传的按钮没有找到"
    
    #编写一个和子页面操作相关的操作
    def frame_(self,data,position):
        '''
        frame:进入子页面
        parent:返回上一级页面
        default:返回顶级页面
        '''
        if data == "frame":
            ele = self.get_position(position)
            if ele!=None:
                self.driver.switch_to.frame(ele)
            else:
                print "要切换的子页面是不存在的"
        elif data == "parent":
            self.driver.switch_to.parent_frame()
        elif data == "default":
            self.driver.switch_to.default_content()
        else:
            print "页面的切换没有这个状态和方法"
    
    #让用户可以自己去设置强制等待的方法
    def sleep_(self,data):
        data = int(data)
        time.sleep(data)
        
    #让用户可以自己去判断自动化的结果是否是成功的，所以需要加上判断结果的函数
    def check_(self,position):
        #检查结果的函数，只需要去尝试获取一下元素即可
        ele = self.get_position(position)
        return ele
    def random_(self,position):
        ele = self.get_position(position)
        str1 = ''
        while True:
            a = chr(random.randint(48,57))
            b = chr(random.randint(65,91))
            c = chr(random.randint(97,123))
            d = random.randint(0,2)
            
            if len(str1)>19:
                break
            if d == 0:
                str1 += a
            elif d == 1:
                str1 += b
            else:
                str1 += c
        if ele!=None:
            ele.clear()
            ele.send_keys(str1)
        else:
            print "输入框没有找到！"
        
    
    
    
    
    
    
    
    
    
    