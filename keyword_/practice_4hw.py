#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import SendKeys
import time
import datetime



driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://app.huawei.com/sdcp/")
def get_position(by,value):
    try:
        ele = WebDriverWait(driver,60,1).until(lambda x:x.find_element(by, value))
    except Exception:
        print "元素没有找到"
        t = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        driver.get_screenshot_as_file("D:/screen/%s.png"%t)
        return None
    else:
        return ele

get_position("id", "tab_phone").click()
get_position("id", "mobile").send_keys("13418685311")
get_position("id", "password").send_keys("12345abcde~")
get_position("class name", "login_submit_pwd").click()


time.sleep(30)
get_position("css selector", ".jalor-button").click()
print '1'
time.sleep(30)
get_position("css selector", ".jalor-dialog-button ").click()
print '2'
source = driver.find_element("css selector", "#navbar>.logo-menu")
action = ActionChains(driver)
action.move_to_element(source).perform()
action.move_to_element(get_position("css selector", "a[data-menu-id='13249']")).perform()
action.click(get_position("css selector", "a[data-menu-id='13255']")).perform()

# 6.点击新增行
get_position("id", "btniGridInsertcus").click()
time.sleep(3)
# 
# 7.输入账号   AISIT_130
get_position("class name", "jalor-button:nth-child(1)").send_keys("AISIT_130")
print '3'
time.sleep(5)
# 8.离开输入焦点，让它自动联想出个人信息
action.move_by_offset(100, 1000).perform()
# 9.选择角色为SE
# 
# 10.可用状态选择为N
# 
# 11.点击保存按钮
# 
# 12.保存成功后，勾选账号，点击标记为删除，点击保存，确定删除成功就完成了














