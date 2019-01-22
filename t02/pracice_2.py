#coding=utf-8
from def_ import *
from selenium.webdriver.common.action_chains import ActionChains
import time
import SendKeys

init_("http://192.168.2.7/ecshop/index.php")
action_("click_","xpath", "//a[contains(.,'请登录')]")
action_("send_keys_", "name", "username", "test")
action_("send_keys_", "name", "password", "123456")
action_("click_", "name", "submit")

action = ActionChains(driver)
source = get_position("xpath", "//div[@id='category_tree']/div[6]/div[@class='cat1']/a")
target = get_position("xpath", "//div[@id='category_tree']/div[6]/div[@class='cat2-box']/div[1]/a")
action.move_to_element(source)
action.click(target)
# action.click("//div[@id='category_tree']/div[6]/div[@class='cat2-box']/div[1]/a")
action.perform()
# time.sleep(2)
# action_("click_", "xpath", "xpath", "//div[@id='category_tree']/div[6]/div[@class='cat2-box']/div[1]/a")

# action_("click_", "xpath", "xpath", "//div[@id='category_tree']/div[6]/div[@class='cat2-box']/div[1]/a")

action_("click_", "class name", "price-btn")
action_("click_", "xpath", "//img[contains(@src,'buybtn1.png')]")
action_("click_", "xpath", "//img[contains(@src,'checkout.gif')]")
for i in range(5):
    SendKeys.SendKeys("{PGDN}")
time.sleep(2)
action_("click_", "xpath", "//input[contains(@src,'bnt_subOrder.gif')]")











