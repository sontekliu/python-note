#!/usr/bin/python
# -*- coding:utf-8 -*-

# 装饰器,类似于java里面的AOP编程
# 定义一个函数，输出其名字，并在调用该函数的时候，打印一行日志

def log(func):
	def wrapper(*args, **kw):
		print 'call function is ', func.__name__
		return func(*args, **kw)
	return wrapper

@log
def show():
	print 'This is show function'
f = show
# 打印函数名称
print f.__name__
#调用函数
f()



