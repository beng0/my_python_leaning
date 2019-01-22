#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import datetime
driver = webdriver.Chrome()
def init_(url):
    driver.get(url)
    driver.implicitly_wait(5)
    driver.maximize_window()
# 获取位置
def get_position(method,position):
    try:
        ele = WebDriverWait(driver,10,1).until(lambda x:x.find_element(method, position))
    except Exception:
        print "元素没有找到"
        t = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        driver.get_screenshot_as_file('D:/screen/%s.png'%t)
        return None
    else:
        return ele
# send_keys操作
# def send_keys_(method,position,content):
#     ele = get_position(method, position)
#     if ele == None:
#         print "输入框没有找到"
#     else:
#         ele.clear()
#         ele.send_keys(content)
# # 点击事件
# def click_(method,position):
#     ele = get_position(method,position)
#     if ele == None:
#         print "元素没有找到"
#     else:
#         ele.click()
#     
# 获取位置并动作
def action_(act,method,position,content=''):
    ele = get_position(method, position)
    if ele == None:
        return
    else:
        if act == "click_":
            ele.click()
        elif act == "send_keys_":
            ele.clear()
            ele.send_keys(content)
        else:
            print "没有这种操作"

















