#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://192.168.2.7/ecshop/admin")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element("name", "username").send_keys("admin")
driver.find_element("name","password").send_keys("12345678a")
driver.find_element_by_class_name("btn-a").click()
driver.switch_to_frame("menu-frame")
driver.find_element_by_css_selector('[href="favourable.php?act=list"]').click()
driver.switch_to_default_content()
driver.switch_to_frame(driver.find_element_by_id("main-frame"))
driver.find_element_by_link_text("添加优惠活动").click()
driver.find_element_by_name("act_name").send_keys(u"新年大促销")

driver.execute_script('document.getElementById("end_time").setAttribute("value","4020-07-08")')
# driver.execute_script('document.getElementById("end_time").removeAttribute("readonly")')
# driver.find_element("id","end_time").clear()
# driver.find_element_by_id("end_time").send_keys("2020-01-01")

driver.find_element_by_css_selector("td>input[value='1']").click()

# driver.find_element_by_name("act_range").click()
# driver.find_element_by_css_selector("select>[value='1']:nth-child(2)").click()

s = Select(driver.find_element_by_name("act_range"))
s.select_by_value('1')

driver.find_element_by_name("keyword").send_keys(u"手机")
driver.find_element_by_name("search").click()
driver.find_element("id","result").click()
driver.find_element("css selector","#result>[value='6']").click()
driver.find_element_by_name("add_range").click()

driver.find_element("id",'min_amount').send_keys("100")
# driver.find_element("id","act_type").click()
# driver.find_element_by_css_selector("#act_type>[value='1']").click()

s = Select(driver.find_element("id","act_type"))
s.select_by_value('1')
driver.find_element("id","act_type_ext").send_keys("50")
driver.find_element_by_css_selector("[type=submit]").click()

















