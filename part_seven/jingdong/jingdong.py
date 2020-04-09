# -*- coding:utf-8 -*-
__author__ = "leo"

import time
import os
import json

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 启动浏览器
from part_seven.jingdong.my_cookies import check_cookies, save_cookies_to_file

# driver = webdriver.Chrome()
# driver.maximize_window()
from part_seven.jingdong.my_mysql import save_goods_info_to_mysql
from part_seven.jingdong.my_mysql import new_save_goods_info_to_mysql


def login(driver):
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


def to_goods_page(driver, name):
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
    if name == "dell":
        # 点击 Dell
        driver.find_element_by_xpath("//a[contains(text(),'DELL')]").click()
    if name == "thinkpad":
        # 点击 thinkpad
        driver.find_element_by_xpath("//li[@id='brand-11518']//img[@class='loading-style2']").click()
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
    # save_goods_info_to_mysql(result_list)
    new_save_goods_info_to_mysql(result_list)


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


def to_start(driver, name):
    # 需要有一个循环操作来控制登陆状态，判断登陆是否成功
    # try:
    #     loop_status = True
    #     while loop_status:
    #         # 检查 cookies 是否生效
    #         login_status = check_cookies(driver)
    #         if login_status:
    #             loop_status = False
    #         else:
    #             login(driver)
    #
    #     # 跳转到商品信息页面
    #     to_goods_page(driver, name)
    # finally:
    #     time.sleep(4)
    #     driver.quit()
    to_goods_page(driver, name)




def thinkpad_start(driver):
    to_start(driver, "thinkpad")


def dell_start(driver):
    to_start(driver, "dell")
