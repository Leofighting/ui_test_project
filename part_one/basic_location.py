# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try:
    # 初始化浏览器
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    time.sleep(2)

    # 使用 id 定位搜索框，并输入内容后回车确认，进行搜索
    # search_element = driver.find_element_by_id("key")
    # search_element.send_keys("华为笔记本")
    # search_element.send_keys(Keys.RETURN)

    # 使用 class 定位，点击 进入秒杀页面
    # seckill_element = driver.find_element_by_class_name("seckill-countdown")
    # seckill_element.click()

    # 使用 link_text 对右侧的京东快报进行点击
    # car_element = driver.find_element_by_link_text("汽车")
    # car_element.click()

    # 使用 partial_link_text 定位农资绿植， 并进行点击
    # cate_menu_element = driver.find_element_by_partial_link_text("农资")
    # cate_menu_element.click()

    # 使用 xpath 定位京东国际，并进行点击
    # navitems_element = driver.find_element_by_xpath("//li[@class='fore9']//a[@class='navitems-lk']")
    # navitems_element.click()

    # 使用 css 选择器定位 我的购物车，并进行点击
    shopping_car_element = driver.find_element_by_css_selector("#settleup")
    shopping_car_element.click()


finally:
    time.sleep(5)
    driver.close()

