#coding=UTF8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element_by_id("kw").send_keys(u"天天向上")
driver.find_element_by_id("su").click()

# driver.find_element_by_id("kw").clear()

driver.find_element("id","kw").send_keys(Keys.BACK_SPACE)

driver.find_element("id","kw").send_keys(Keys.CONTROL,"a")

driver.find_element("id","kw").send_keys(Keys.CONTROL,"c")
driver.find_element("id","kw").clear()
for i in range(5):
    driver.find_element("id","kw").send_keys(u"哈哈，你是个大傻逼")
driver.find_element("id","su").send_keys(Keys.ENTER)

driver.find_element("id","kw").clear()
driver.find_element("id","kw").send_keys(u"eclipse快捷键")
driver.find_element("id","su").click()
time.sleep(3)
driver.find_element_by_css_selector("h3.t>a").click()
driver.find_element_by_css_selector("body div.post").send_keys(Keys.CONTROL,"a")









