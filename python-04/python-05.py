#!/usr/bin/python
# -*- coding:utf-8 -*-

# 返回函数，即，函数作为返回值返回
def lazy_sum(*args):
	def inner_sum():
		ax = 0
		for x in args:
			ax = ax + x
		return ax
	return inner_sum

f = lazy_sum(1,2,3,4,5)
print (f)
print (f())

def count():
	fs = []
	for i in range(1, 5):
		def f():
			return i * i
		fs.append(f)
	print fs
	return fs

f1, f2, f3, f4 = count()

print f1(), f2(), f3()





















































