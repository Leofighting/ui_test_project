# -*- coding:utf-8 -*-
__author__ = "leo"


class Field:

    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type


class StringField(Field):
    def __init__(self, column_name):
        super().__init__(column_name, "varchar(200)")


class IntegerField(Field):
    def __init__(self, column_name):
        super(IntegerField, self).__init__(column_name, "bigint")


class TextField(Field):
    def __init__(self, column_name):
        super().__init__(column_name, "text")