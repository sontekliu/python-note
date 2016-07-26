#!/usr/bin/python
# -*- coding:utf-8 -*-

# 匿名函数
# lambda x : x * x
# 关键字 lambda 标识的是匿名函数，冒号前面的x表示函数参数
# 匿名函数特点，只能有一个表达式，不用写return，表达式的结果就是返回值

# 可以把匿名函数赋值一个变量，使用该变量来调用该函数
f = lambda x : x * x
print f(8)

# 匿名函数也可以作为返回值返回

def build(x, y):
	return lambda : x * x + y * y

aa = build(4, 5)
print aa
print aa()
