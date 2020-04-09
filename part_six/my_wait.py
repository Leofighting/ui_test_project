# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://passport.jd.com/new/login.aspx")

# 强制等待
# time.sleep(3)

# 隐性等待
# 设置一个最长的等待，假设在规定的时间内网页加载完成，则执行下一步
# 否则一直等待到时间截止，然后执行下一步
# 只要设置一次，就会在 driver 的整个生命周期存在
# driver.implicitly_wait(10)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 定位元素
locator = (By.CSS_SELECTOR, ".login-tab.login-tab-r")
# 判断元素是否存在
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
element.click()
driver.quit()