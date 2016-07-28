#!/usr/bin/python
# -*- coding:utf-8 -*-

class Student(object):
	pass

# 定义一个类，class表示是类，后面是类名，通常大写字母开头，紧接着是(object)，
# 表示是从哪儿个类继承下来，没特殊情况就使用object类，所有类最终都会继承的类

# 创建类的实例
s = Student()
print s
print Student

# 可以自由的给实例变量绑定属性，如：
s.name = 'abc'
print s.name

# 定义__init__方法，在创建实例的时候就把相应的属性加入，如:
# 类中的方法第一个参数都是self，其他参数和普通函数一样
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_stu(self):
		print self.name, self.score

s = Student('zhangsan', 89)
print s.name
print s.score
s.print_stu()





