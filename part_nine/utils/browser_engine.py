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
    def init_remote_driver():
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT

        result_dict = {}

        for name, url in remote_browser_dict:
            option = webdriver.ChromeOptions()
            option.add_argument("disable-infobars")
            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver

        return result_dict
