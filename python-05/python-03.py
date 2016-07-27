#!/usr/bin/python
# -*- coding:utf-8 -*-

# python 安装第三方模块

# python中安装第三方模块是通过setuptools工具完成，easy_install和pip都封装了setuptools这个工具，推荐使用pip

# pip 安装第三方模块

# pip install MySQL-python

# 模块搜索路径,当python试图加载一个模块时，python会在指定的路径下面搜索，如果找不到就报错。
# 路径包括:当前目录，已安装的内置模块、第三方模块

import sys

print sys.path

