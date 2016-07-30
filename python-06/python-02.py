#!/usr/bin/python
# -*- coding:utf-8 -*-

# python 类中元素的访问限制

# 在Class内部，可以有属性和方法，外部代码可以直接调用实例变量的方法和属性，
# 如果让内部的属性不被外部访问，可以把属性的名称前加上两个下划线“__”，在
# python中，如果实例变量以"__"开头，则表示是私有变量，只有内部可以访问。
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score 
	
	# 提供访问属性的方法
	def get_score(self):
		return self.__score
	
	# 提供给属性设置值的方法
	def set_score(self, score):
		self.__score = score

	def print_stu(self):
		print self.__name, self.__score

s  = Student("abc", 34)
s.print_stu()

# 在python中，变量名以__xxx__命名的，即，双下划线开头，双下划线结尾的是特殊变量，
# 特殊变量可以被访问，不是private的。
# 以下划线开头的变量，如_name，这样是可以被外部访问的，但是当看到这样的变量时，
# 意思就是，“虽然我可以被访问，但是，请把为视为私有变量，不要随意访问"






