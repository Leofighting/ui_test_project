# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import time
from selenium import webdriver
import json

# 初始化浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()


def save_cookies(driver):
    """保存cookies"""
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    # 从 driver 中获取 cookies
    cookies = driver.get_cookies()
    with open(file_path + "jd.cookies", "w") as f:
        # 使用 json.dump 方法写入文件
        json.dump(cookies, f)

    print(cookies)


def login():
    try:
        # 打开京东首页
        driver.get("https://www.jd.com/")
        time.sleep(1)
        driver.find_element_by_class_name("link-login").click()
        time.sleep(1)
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").send_keys("")
        driver.find_element_by_id("nloginpwd").send_keys("")
        driver.find_element_by_id("loginsubmit").click()
        save_cookies(driver)

    finally:
        time.sleep(3)
        driver.close()


if __name__ == '__main__':
    login()