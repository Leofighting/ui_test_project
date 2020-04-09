# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from part_nine.config import basic_config


class BasePage:
    def __init__(self, driver, url):
        """
        BasePage 的构造方法
        :param driver: 启动具体哪个浏览器
        :param url: 目标的url 地址
        """
        self._driver = driver
        self._url = url

    def open(self):
        """
        页面打开方法
        :return: 返回一个 浏览器的 driver
        """
        self._driver.get(url=self._url)
        return self._driver

    def find_element(self, *locator, element=None, timeout=None,
                     wait_type="visibility", when_failed_close_browser=True):
        """
        查找元素，分别支持以 driver 或 element 之上来进行查找元素
        :param locator: 元素定位方式；数据类型是元祖；例如(By.ID, "id_value")
        :param element: 页面元素，默认为 None
        :param timeout: 超时时间，默认值为 None 时，直接获取配置文件中的值
        :param wait_type: 等待类型，支持两种方式：1、直到元素可见；2、直到元素存在
        :param when_failed_close_browser: 当元素获取失败时，浏览器是否关闭
        :return:
        """
        if element is not None:
            return self._init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))

        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_element_located(*locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_element_located(*locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式是：{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式是：{}".format(locator))

    def find_elements(self, *locator, element=None, timeout=None,
                      wait_type="visibility", when_failed_close_browser=True):
        """
        查找元素合集
        :param locator: 元素定位方式；数据类型是元祖；例如(By.ID, "id_value")
        :param element: 页面元素，默认为 None
        :param timeout: 超时时间，默认值为 None 时，直接获取配置文件中的值
        :param wait_type: 等待类型，支持两种方式：1、直到元素可见；2、直到元素存在
        :param when_failed_close_browser: 当元素获取失败时，浏览器是否关闭
        :return: 返回定位的元素集
        """
        if element is not None:
            return element.find_elements(*locator)

        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式是：{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式是：{}".format(locator))

    def _init_wait(self, timeout):
        if not timeout:
            return WebDriverWait(driver=self._driver, timeout=basic_config.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
