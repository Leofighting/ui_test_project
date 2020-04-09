# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.12306.cn/index/")

time.sleep(2)

from_element = driver.find_element_by_id("fromStationText")
from_element.click()
time.sleep(2)
from_element.send_keys("广州")
driver.find_element_by_xpath("//*[text()='广州南']").click()

to_element = driver.find_element_by_id("toStationText")
to_element.click()
time.sleep(2)
to_element.send_keys("深圳")
driver.find_element_by_xpath("//*[text()='深圳西']").click()

# 移除 readonly 属性
js = "$('input[id=train_date]').removeAttr('readonly')"
driver.execute_script(js)
date_element = driver.find_element_by_id("train_date")
date_element.click()
date_element.clear()
date_element.send_keys("2020-04-10")
time.sleep(2)

# 点击查询按钮，以为存在元素遮挡问题，需要提前点击其他地方，清除遮挡
driver.find_element_by_class_name("form-label").click()
time.sleep(1)
driver.find_element_by_id("search_one").click()
time.sleep(5)
driver.quit()