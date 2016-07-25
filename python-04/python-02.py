#!/usr/bin/python
# -*- coding:utf-8 -*-

# map AND reduce

# map函数，接收两个参数，第一个是函数，第二个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
def f(x):
	return x * x
r = map(f, [1,2,3,4,5])
print r
print map(str, [1,2,3,4,5])


# reduce，reduce是把函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个
# 元素做累积计算，例如：
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
	return x * 10 + y
print reduce(add, [1,2,3,4])

# str2int 字符串--> 整型

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn, map(char2num, s))
print str2int('234789')

# 练习1， 输入['sontek','LIST','mAp'] 输出 ['Sontek','List','Map']
def first2big(x):
	# 首字母大写
	return x.capitalize()
print map(first2big, ['sontek', 'LIST', 'mAp'])

# 练习2， 求list所有元素的积
def prod(x, y):
	return x * y
print reduce(prod, [1,2,3,4,5,6])








