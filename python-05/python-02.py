#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'javaliu'

# 导入模块
import sys

def test():
	# 命令行执行时的所有参数，例如: python python-02.py aa bb 参数为 python-02.py、aa、bb
	args = sys.argv
	if len(args) == 1:
		print 'this is one args'
	elif len(args) == 2 :
		print 'Hello,', args[0]
	else:
		print 'Too many arguments'

# 直接执行该文件的时候，执行test()函数，而作为模块导入的时候if判断是False，
# 这种if最常用的作用就是用于测试
if __name__ == '__main__':
	test()

# 模块别名
# StringIO 和 cStringIO是两个模块，这两个模块接口和功能是一样的，但是cStringIO是C语言写的，速度更快
# 所以经常有如下写法: 
# import cStringIO as StringIO
# 这样如果有的平台不提供cStringIO则可以使用StringIO，因为接口和功能都一样

# 作用域
# 在模块中需要定义很多变量和函数，有些提供外部调用，有的仅仅是提供内部使用。如果仅仅是内部使用，则
# 使用“_”作为标识，以"_"命名的函数或者变量就认为是私有的，类似有Java里面的private方法，但是python
# 并不能完全限制私有函数或者变量的访问。




