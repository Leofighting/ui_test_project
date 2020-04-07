# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 初始化浏览器
driver = webdriver.Chrome()


def screenshot(driver, file_path=None):
    if not file_path:
        project_path = os.path.dirname(os.getcwd())
        file_path = project_path + "/images/"
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        image_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".png"
        file_path = file_path + image_name
        print(file_path)
    driver.save_screenshot(file_path)


try:
    # 窗口最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    time.sleep(3)
    # 鼠标悬停
    element = driver.find_element_by_link_text("手机")
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(3)
    old_phone = driver.find_element_by_link_text("老人机")
    old_phone.click()
    # driver.save_screenshot("laorenji.png")
    # 浏览器句柄切换
    handles = driver.window_handles
    current_handle = driver.current_window_handle
    for handle in handles:
        if handle != current_handle:
            driver.switch_to.window(handle)
            screenshot(driver)


finally:
    time.sleep(5)
    driver.close()
