# -*- coding:utf-8 -*-
__author__ = "leo"

from part_nine.orm.orm import Model


class Goods(Model):
    computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")