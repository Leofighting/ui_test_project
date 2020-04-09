# -*- coding:utf-8 -*-
__author__ = "leo"

from part_seven.field import Field, StringField, TextField
from part_seven.orm import Model


class Goods(Model):
    computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")


goods = Goods()
goods.insert(["computer_part", "computer_info"], ["组件", "组件信息"])


# class Goods:
#     computer_part = StringField("computer_part")
#     computer_info = TextField("computer_info")