# -*- coding:utf-8 -*-
__author__ = "leo"

import json
import os


def save_cookies_to_file(driver):
    """把 cookies 保存到文件中"""
    # 获取存储 cookies 的文件夹
    file_path = get_cookies_dir()

    # 获取 cookies
    cookies = driver.get_cookie()

    # 存储 cookies 到文件中
    with open(file_path + "jd.cookies", "w") as f:
        json.dump(cookies, f)


def get_cookies_dir():
    """获取 cookies 的文件夹"""
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path


def check_cookies(driver):
    """检查是否有 cookies """
    # 设置一个登陆状态，初始值是未登录
    login_status = False

    # 将 cookies 信息保存在 driver 中
    driver = save_cookies_to_driver(driver)

    # 进行跳转连接检测
    check_url = "https://order.jd.com/center/list.action"
    driver.get(check_url)
    current_url = driver.current_url
    if current_url == check_url:
        login_status = True
    return login_status


def save_cookies_to_driver(driver):
    """保存 cookies 到 driver 中"""
    cookies_file = get_cookies_file()
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 清除旧的 cookies
    driver.get("https://www.jd.com/")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        if cookie.get("expiry"):
            cookie.pop("expiry")
        driver.add_cookie(cookie)
    return driver


def get_cookies_file():
    return get_cookies_dir() + "jd.cookies"

