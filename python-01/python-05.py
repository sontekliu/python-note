#!/usr/bin/python
#-*- coding:utf-8 -*-
# python 条件判断和循环学习
x = 1
x = [1]
x = 'abc'
x = (2,3,4)
x = {'key':'abc'}
x = {}
# 只要x是非零数值，非空字符串，非空list，非空tuple，非空字典，就为True，否则为False
if x:
	print x

# for 循环

sum = 0
for x in range(101):
	sum = sum + x
print sum

name = ['wangwu','zhangsan','lisi']
for x in name:
	print x,


sum = 0
n = 100
while n > 0:
	sum = sum + n
	n = n - 1
print sum
