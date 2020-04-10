# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from part_nine.config import basic_config


class BrowserEngine:
    @staticmethod
    def init_local_driver():
        option = webdriver.ChromeOptions()
        option.add_argument("disable-infobars")
        driver = webdriver.Chrome(chrome_options=option)
        return driver

    @staticmethod
    def init_local_driver_no_gui():
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")  # 无界面运行设置
        driver = webdriver.Chrome(chrome_options=option)
        return driver

    @staticmethod
    def init_remote_driver():
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT

        result_dict = {}

        for name, url in remote_browser_dict:
            options = webdriver.ChromeOptions()
            options.add_argument("disable-infobars")
            driver = webdriver.Remote(
                options=options,
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver

        return result_dict

    @staticmethod
    def init_remote_driver_no_gui():
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT

        result_dict = {}

        for name, url in remote_browser_dict:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # 无界面运行设置
            driver = webdriver.Remote(
                options=options,
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver

        return result_dict
