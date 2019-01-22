#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
import SendKeys
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://192.168.2.7/ecshop/admin")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element("name", "username").send_keys("admin")
driver.find_element("name","password").send_keys("12345678a")
# driver.find_element("css selector", "[type=submit]").click()
WebDriverWait(driver,30,1).until(lambda a:a.find_element("css selector","[type=submit]")).click()

# 2.点击进入添加新商品菜单
driver.switch_to.frame("menu-frame")
driver.find_element("css selector", "[href='goods.php?act=add']").click()
# 3.输入商品名称
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")
driver.find_element("css selector", "[name=goods_name]").send_keys(u"手机")

# 4.选择任何一个字体颜色
driver.find_element("id", "font_color").click()
driver.find_element("css selector", "[bgcolor='#FE0000']").click()
# 5.选择商品分类
s = Select(driver.find_element("name", "cat_id"))
s.select_by_value("4")
# 6.选择商品售价
driver.find_element("name", "market_price").send_keys("400.11")
driver.find_element("css selector", "[value='取整数']").click()

# 7.勾选促销价的复选框
driver.find_element("xpath", "//label[@for='is_promote']").click()
# 8.修改促销价的结束时间为2020-10-10
driver.execute_script('document.getElementById("promote_end_date").setAttribute("value","2020-10-10")')

# 9.点击选择文件，上传一张商品图片
# driver.find_element("name", "goods_img").click()
WebDriverWait(driver,30,1).until(lambda x:x.find_element("name","goods_img")).click()
time.sleep(2)
SendKeys.SendKeys(r"D:\1.jpg")
time.sleep(2)
SendKeys.SendKeys("{ENTER}")

SendKeys.SendKeys("{ENTER}")

# 10.点击确定按钮
driver.find_element("xpath", "//div[@class='button-div']/input[2]").click()


























