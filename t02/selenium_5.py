#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://mail.qq.com")
driver.maximize_window()
driver.implicitly_wait(15)

driver.switch_to_frame("login_frame")
driver.find_element_by_id("img_out_2397990387").click()

#点击写信按钮
driver.find_element_by_id("composebtn").click()

# 填写收件人
driver.switch_to_frame(driver.find_element_by_xpath("//div[@id='mainFrameContainer']/iframe"))
action = ActionChains(driver)
action.click(driver.find_element_by_id("toAreaCtrl"))
action.send_keys("24763563@qq.com")
time.sleep(5)
action.perform()

# time.sleep(10)


# 填写主题
driver.find_element_by_name("subject").send_keys(u"哈哈航")
 
# 填写内容
driver.switch_to_frame(driver.find_element_by_xpath("//div[@id='QMEditorArea']//iframe"))
 
driver.find_element_by_css_selector("[accesskey='q']").send_keys("hello world")
 
# 点击发送按钮
driver.switch_to.parent_frame()
driver.find_element("name","sendbtn").click()






