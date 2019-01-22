#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import SendKeys

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()


# 进入禅道的页面
# http://192.168.2.7:81/zentao
driver.get("http://192.168.2.7:81/zentao")
# admin
# 123456
driver.find_element("id", "account").send_keys("admin")
driver.find_element("name", "password").send_keys("123456")
driver.find_element("id","submit").click()
# 
# 点击主菜单的测试
driver.find_element("xpath", "//a[@href='/zentao/qa/']").click()
# 
# 点击副菜单的bug
driver.find_element("xpath", "//a[@href='/zentao/bug-browse-3.html']").click()
# 
# 点击提BUG
driver.find_element("xpath", "//a[@href='/zentao/bug-create-3-0-moduleID=0.html']").click()
# 在版本中选择trunk
driver.find_element("css selector", "#buildBox ul[class=chosen-choices]").click()
driver.find_element("css selector", "#buildBox div .chosen-drop").click()
# 操作系统选择windows 7
s = Select(driver.find_element("id", "os"))
s.select_by_index(4)
# 
# 填写标题
driver.find_element("css selector", ".input-group.w-p100 [id=title]").send_keys(u"登录失败")
# 
# 填写步骤、结果、期望

driver.switch_to_frame(driver.find_element("xpath", "//iframe[@class='ke-edit-iframe']"))
action = ActionChains(driver)
action.click(driver.find_element("xpath", "//body[contains(@class,'article-conten')]/p[contains(.,'步骤')]"))
action.send_keys(u"步骤")
action.click(driver.find_element("xpath", "//body[@class='article-content']/p[contains(.,'结果')]"))
action.send_keys(u"结果")
action.click(driver.find_element("xpath", "//body[@class='article-content']/p[contains(.,'期望')]"))
action.send_keys(u"期望结果")
# driver.find_element("xpath", "//body[@class='article-content']").clear()
# time.sleep(2)
# action.send_keys(u"[步骤]\n1.步骤一\n2.步骤2\n3.步骤3\n[结果]\n结果不能够登录了。\n[期望]\n期望能够登录")
action.perform()
# 
# 上传附件
driver.switch_to.parent_frame()
# time.sleep(3)
SendKeys.SendKeys("{PGDN}")
time.sleep(3)
SendKeys.SendKeys("{PGDN}")
SendKeys.SendKeys("{PGDN}")

# driver.find_element("name","files[]").click()
# time.sleep(1)
# SendKeys.SendKeys(r"D:\111.txt")
# # time.sleep(1)
# 
# time.sleep(2)
# SendKeys.SendKeys("{ENTER}")
# SendKeys.SendKeys("{ENTER}")
driver.find_element("name", "files[]").send_keys(r"D:\111.txt")  #input框可直接输入文件名和路劲上传文件
# 点击保存
driver.find_element("id","submit").click()













