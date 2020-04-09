# -*- coding:utf-8 -*-
__author__ = "leo"


def set_mysql_config(env):
    if env == "dev":
        db_config = {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "123qwe",
            "db": "python_ui",
            "port": 3306,
            "charset": "utf8"
        }
    elif env == "pro":
        db_config = {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "123qwe",
            "db": "python_ui",
            "port": 3306,
            "charset": "utf8"
        }

    return db_config
