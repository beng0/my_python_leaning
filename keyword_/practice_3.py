#coding=utf-8
# from t02.def_ import *
# from runBrower import *
# 
# r = Brower()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime
import SendKeys


driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://test.umaicloud.com")
def get_position(by,value):
    try:
        ele = WebDriverWait(driver,30,1).until(lambda x:x.find_element(by, value))
    except Exception:
        print "元素没有找到"
        t = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        driver.get_screenshot_as_file("D:/screen/%s.png"%t)
        return None
    else:
        return ele

get_position("name", "account").send_keys()
get_position("name", "account").send_keys("13418685311")
get_position("name","pwd").send_keys("12345678a")
get_position("xpath", "//span[text()='登录']").click()

get_position("xpath", "//span[text()='采购']").click()


# 2.进入采购页面，点击添加采购计划
get_position("xpath", "(//span[text()='添加采购计划'])[1]").click()
# 3.点击添加采购商品
get_position("xpath", "//span[text()='采购商品']/../button/i").click()
# 4.搜索自己是商品，点击搜索按钮
get_position("css selector", "[placeholder='搜索SKU、品名']").send_keys("iamsingleone")
get_position("xpath", "(//span[text()='搜索'])[2]").click()
time.sleep(5)
get_position("css selector", ".el-dialog__body .el-table__fixed>.el-table__fixed-header-wrapper label span").click()
# driver.execute_script("document.querySelector('.el-dialog__body .el-table__fixed>.el-table__fixed-header-wrapper label').className+=' is-checked'")
# (//input[@class='el-checkbox__original'])[13]/..
time.sleep(1)
# 5.点击确定按钮
get_position("xpath", "(//span[text()='确定'])[1]").click()
# 6.输入计划采购量，点击提交审核
get_position("css selector", ".el-form-item__content input").send_keys("1")
time.sleep(1)
get_position("xpath", "//div[@class='el-dialog__footer']//span[text()='提交审核']").click()
# for i in range(4):
#     SendKeys.SendKeys("{TAB}")
#     time.sleep(1)
# SendKeys.SendKeys("{ENTER}")































