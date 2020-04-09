# -*- coding:utf-8 -*-
__author__ = "leo"

from part_seven.field import Field
from part_seven.my_database import create_pool


class ModelMetaClass(type):
    """创建模型元类"""

    def __new__(cls, table_name, bases, attrs):
        """

        :param table_name: 类名，对应数据库的表名
        :param bases: 父类的元祖
        :param attrs: 类的属性方法
        """
        if table_name == "Model":
            return super().__new__(cls, table_name, bases, attrs)

        mappings = dict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                mappings[key] = value

        for key in mappings.keys():
            attrs.pop(key)

        attrs["__table__"] = table_name.lower()

        attrs["__mappings__"] = mappings
        return super().__new__(cls, table_name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def insert(self, column_list, param_list):
        print("执行了insert方法")
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("这个字段没有发现 field not found")

        # 检查参数的合法性
        args = self.__check_params(param_list)
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(column_list), ",".join(args))
        res = self.__do_execute(sql)
        print(res)

    def __check_params(self, param_list):
        args = []
        for param in param_list:
            if "\"" in param:
                param = param.replace("\"", "\\\"")
            param = "\"" + param + "\""
            args.append(param)
        return args

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.cursor()
        print(sql)
        if "select" in sql:
            cur.execute(sql)
            result = cur.fetchall()
        else:
            result = cur.execute(sql)
        conn.commit()
        cur.close()
        return result

    def select(self, column_list, where_list):
        print("调用select方法")
        args = []
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)
        for key in where_list:
            args.append(key)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        sql = "select %s from %s where %s" % (",".join(column_list), self.__table__, " and ".join(args))
        result = self.__do_execute(sql)
        return result

    def update(self, set_column_list, where_list):
        print("调用 update 方法")
        args = []
        fields = []

        for key in set_column_list:
            fields.append(key)

        for key in where_list:
            args.append(key)

        for key in set_column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        sql = "update %s set %s where %s" % (self.__table__, ",".join(set_column_list), " and ".join(args))

        res = self.__do_execute(sql)
        return res

    def delete(self, where_list):
        print("调用 delete 方法")
        args = []
        for key in where_list:
            args.append(key)
        sql = "delete from %s where %s" % (self.__table__, " and ".join(args))

        res = self.__do_execute(sql)
        return res
