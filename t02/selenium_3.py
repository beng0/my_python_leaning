#coding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.ituring.com.cn/")
driver.maximize_window()
driver.find_element_by_link_text(u"登录").click()
driver.find_element("id","Email").send_keys("adamconan@163.com")
driver.find_element_by_id("Password").send_keys("123456")
driver.find_element_by_css_selector('label[for=RememberMe]').click()
driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_class_name("go").click()

driver.quit()



