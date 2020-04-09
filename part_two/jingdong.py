# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import os
import json

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 启动浏览器
driver = webdriver.Chrome()
driver.maximize_window()


def login():
    driver.get("https://www.jd.com/")
    time.sleep(2)
    driver.find_element_by_class_name("link-login").click()
    time.sleep(2)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("18819151992")
    driver.find_element_by_id("nloginpwd").send_keys("5love01314")
    driver.find_element_by_id("loginsubmit").click()
    # 将 cookies 保存到文件中
    save_cookies_to_file(driver)


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


def check_cookies():
    """检查是否有 cookies """
    # 设置一个登陆状态，初始值是未登录
    login_status = False

    # 将 cookies 信息保存在 driver 中
    driver = save_cookies_to_driver()

    # 进行跳转连接检测
    check_url = "https://order.jd.com/center/list.action"
    driver.get(check_url)
    current_url = driver.current_url
    if current_url == check_url:
        login_status = True
    return login_status


def save_cookies_to_driver():
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


def to_goods_page():
    # 把页面放在首页上
    driver.get("https://www.jd.com/")

    # 定位到 电脑 元素上
    computer_element = driver.find_element_by_link_text("电脑")

    # 鼠标悬停在 电脑 元素上
    ActionChains(driver).move_to_element(computer_element).perform()

    # 点击 笔记本 元素
    time.sleep(2)
    driver.find_element_by_link_text("笔记本").click()

    # 切换句柄
    handles = driver.window_handles
    index_handle = driver.current_window_handle
    for handle in handles:
        if handle != index_handle:
            driver.switch_to.window(handle)

    # 点击 Dell
    driver.find_element_by_xpath("//a[contains(text(),'DELL')]").click()
    # 点击 7000以上
    driver.find_element_by_xpath("//div[@id='J_selectorPrice']//a[contains(text(),'7000')]").click()
    # 点击 评论数
    driver.find_element_by_xpath("//div[@class='f-line top']//a[3]").click()
    # 点击 第一款电脑
    driver.find_element_by_xpath("//div[@id='J_searchWrap']//li[1]//div[1]//div[1]//a[1]//img[1]").click()
    # 切换句柄
    notebook_handle = driver.current_window_handle
    handles = driver.window_handles

    for handle in handles:
        if handle != index_handle and handle != notebook_handle:
            driver.switch_to.window(handle)
    # 点击规则与包装
    time.sleep(3)
    js = "window.scrollTo(0, 1500)"  # 向下滚动
    driver.execute_script(js)
    driver.find_element_by_xpath("/html[1]/body[1]/div[10]/div[2]/div[1]/div[1]/ul[1]/li[2]").click()
    # 解析所有的标签
    info_elements = driver.find_elements_by_class_name("Ptable-item")
    result_list = []
    for info_element in info_elements:
        info_element_dict = get_info_element_dict(info_element)
        result_list.append(info_element_dict)
    # 保存这些信息到文件中
    save_goods_info(result_list)


def get_info_element_dict(info_element):
    """获取 元素 中所有文本信息"""
    # 获取第一列的信息
    computer_part = info_element.find_element_by_tag_name("h3")
    # 计算机信息中的 key 值
    computer_info_keys = info_element.find_elements_by_tag_name("dt")
    # 计算机信息中的 value 值
    computer_info_values = info_element.find_elements_by_xpath("dl//dd[not(contains(@class, 'Ptable-tips'))]")

    # 存储计算机信息的key 和 value
    key_and_value_dict = {}
    # 存储所有的计算机组成信息
    parts_dict = {}

    for i in range(len(computer_info_keys)):
        key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

    parts_dict[computer_part.text] = key_and_value_dict

    return parts_dict


def save_goods_info(info_list):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/goods_infos/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    with open(file_path + "computer.infos", "a", encoding="utf-8") as f:
        f.write(str(info_list))
        print(str(info_list))


if __name__ == '__main__':
    # 需要有一个循环操作来控制登陆状态，判断登陆是否成功
    try:
        loop_status = True
        while loop_status:
            # 检查 cookies 是否生效
            login_status = check_cookies()
            if login_status:
                loop_status = False
            else:
                login()

        # 跳转到商品信息页面
        to_goods_page()
    finally:
        time.sleep(4)
        driver.quit()
