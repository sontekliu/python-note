#!/usr/bin/python
# -*- coding:utf-8 -*-

# 函数本身可以赋值给变量，变量可以指向函数
f = abs
print f(-10)
# 总结，函数名其实就是指向函数的变量

# 函数作为函数参数，这种函数就称之为高阶函数

def fun(x):
	return abs(x)

def fun_adv(x, y, f):
	return f(x) + f(y)

print fun_adv(10,20, fun)
print fun_adv(10,-320, fun)




