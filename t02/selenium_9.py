#coding=utf-8

from def_ import *
import selenium.webdriver.common.keys
import SendKeys
from selenium.webdriver.common.action_chains import ActionChains
import time
# from selenium.webdriver.support.wait import WebDriverWait

# init_("https://www.baidu.com")
# # get_position("id", "kw").send_keys("python")
# # get_position("id","su").click()
# # send_keys_("id","kw11","python")
# # click_("id", "su")
# # click_("name", "tj_trnews")
# action_("send_keys_", "id", "kw1", "python")
# action_("click_", "id", "su")
# action_("click_", "name", "tj_trnews")

## js弹出框
# init_("http://192.168.2.7/ecshop/index.php")
# action_("send_keys_","id", "keyword", u"双肩包")
# action_("click_","name","imageField")
# action_("click_","xpath","//img[contains(@alt,'学院风简约')]")
# action_("click_","xpath","//img[contains(@src,'buybtn1.png')]")
# action_("click_","link text","删除")


# SendKeys.SendKeys("{ENTER}")
# js = driver.switch_to_alert()
# print js.text
# # js.accept()
# js.dismiss()


init_("https://www.tmall.com/")
action_("click_", "link text", "淘宝网")
h = driver.window_handles
driver.switch_to_window(h[-1])
action_("click_","link text","免费注册")
action_("click_","id","J_AgreementBtn")
action_("send_keys_","id","J_Mobile","13000000000")
time.sleep(2)
action = ActionChains(driver)
# source = get_position("id", "nc_1_n1z")
# target = get_position("link text","中文")
source = driver.find_element_by_id("nc_1_n1z")
# target = driver.find_element_by_link_text("中文")
# action.drag_and_drop(source, target)
# action.drag_and_drop_by_offset(source, 260, 0)

action.click_and_hold(source)
action.move_by_offset(260, 0)
action.release()
action.perform()




















