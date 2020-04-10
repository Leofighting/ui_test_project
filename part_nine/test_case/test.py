# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.webdriver.common.by import By

from part_nine.pages.goods_info_page import GoodsInfoPage
from part_nine.utils.browser_engine import BrowserEngine
from part_nine.config import logging_setting
from part_nine.pages.goods_list_page import GoodsListPage


class Test:
    driver = BrowserEngine.init_local_driver()
    logger = logging_setting.get_logger()

    def test_save_info(self):
        self.logger.debug("目标保存电脑详情信息")
        goods_list_page = GoodsListPage(self.driver)
        goods_list_page.get_goods_list_driver("电脑", "笔记本")

        brand_locator = (By.ID, "brabd-11518")
        price_locator = (By.LINK_TEXT, "7000以上")
        comment_locator = (By.LINK_TEXT, "评论数")
        goods_list_page.get_selector_page([brand_locator, price_locator, comment_locator])

        self.logger.debug("开始获取具体的商品页面")

        goods = (By.XPATH, "//div[@id='J_searchWrap']//li[1]//div[1]//div[1]//a[1]//img[1]")
        driver = goods_list_page.get_goods_info_page(goods)
        self.logger.info("当前的url地址是：", driver.current_url)
        goods_info = GoodsInfoPage(driver)
        goods_info.save_product_info()
        self.logger.debug("保存商品信息成功")


t = Test()
t.test_save_info()