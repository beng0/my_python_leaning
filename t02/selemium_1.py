#coding=utf-8

from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5) #全局超时5秒
driver.back()
time.sleep(2) #添加休眠时间
driver.forward()
time.sleep(2)
driver.refresh()
# driver.close() # 关闭浏览器但是不停止进程
driver.quit()  # 关闭浏览器并退出进程