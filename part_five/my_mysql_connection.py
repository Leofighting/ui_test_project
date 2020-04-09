# -*- coding:utf-8 -*-
__author__ = "leo"

import pymysql

# 获取 mysql 连接
db_connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="123qwe",
    database="python_ui",
    charset="utf8"
)
# 获取游标
cursor = db_connection.cursor()
# 书写 SQL
sql = "insert into goods(computer_part, computer_info) values (" \
      "'主体', '主体信息')"
# 执行 SQL
cursor.execute(sql)
# 提交 SQL
db_connection.commit()
# 关闭游标
cursor.close()
# 关闭连接
db_connection.close()
