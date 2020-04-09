# -*- coding:utf-8 -*-
__author__ = "leo"

import sys
import logging

# logging 模块，默认等级是 warning
# logging.basicConfig(level=10)
#
# logging.debug("this is debug logging")  # 调试信息，打印最详细的一个级别，用于协助调试程序
# logging.info("this is info logging")  # 日志详细信息，打印频率比 debug 稍低，一般生产环境开启
# logging.warning("this is warning logging")  # 警告信息，当程序已经发生错误是触发，但不影响程序运行
# logging.error("this is error logging")  # 错误信息，影响程序运行

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y%m%d %H:%M:%S"
#
# logging.basicConfig(filename="first.log",
#                     level=10,
#                     format=LOG_FORMAT,
#                     datefmt=DATE_FORMAT)
#
# logging.debug("debug logging")

file_path = "second.log"
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 文件日志的配置
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler(file_path, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 控制台的日志配置
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("这是日志信息")
