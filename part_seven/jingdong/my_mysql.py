# -*- coding:utf-8 -*-
__author__ = "leo"

import pymysql

from part_seven.model import Goods


def save_goods_info_to_mysql(info_list):
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        for info in info_list:
            for key, value in info.items():
                sql = "insert into goods(computer_part, computer_info) " \
                      "values (\"%s\", \"%s\")" %(key, value)

                print(sql)
                cursor.execute(sql)
                db_connection.commit()

    finally:
        close_db(db_connection, cursor)


def get_connection():
    db_connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123qwe",
        database="python_ui",
        charset="utf8"
    )
    return db_connection


def close_db(db_connection, cursor):
    cursor.close()
    db_connection.close()


def new_save_goods_info_to_mysql(info_list):
    goods = Goods()

    for info in info_list:
        for key, value in info.items():
            goods.insert(["computer_part", "computer_info"], [str(key), str(value)])
