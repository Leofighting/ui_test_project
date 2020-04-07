# -*- coding:utf-8 -*-
__author__ = "leo"

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

try:
    # 初始化浏览器
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    time.sleep(3)

    # 鼠标悬停事件
    # car_element = driver.find_element_by_link_text("汽车")
    # ActionChains(driver).move_to_element(car_element).perform()
    # time.sleep(4)
    # mic_car_element = driver.find_element_by_link_text("微型车")
    # mic_car_element.click()

    # 键盘事件
    search_element = driver.find_element_by_id("key")
    search_element.send_keys("华为笔记本")
    search_element.send_keys(Keys.RETURN)

finally:
    time.sleep(5)
    driver.close()