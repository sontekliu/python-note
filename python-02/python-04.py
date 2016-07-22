#!/usr/bin/python
# -*- coding:utf-8 -*-

# 递归函数，如果一个函数在函数内部调用了自身，那么这个函数就是递归函数

def fact(n):
	if 1 == n:
		return 1
	return n * fact(n-1)

print fact(10)
print fact(100)
# 栈溢出
print fact(1000)

# 尾递归是指，在函数返回的时候，调用自身本身，并且return语句不能包含表达式。
# 这样，编译器或者解释器就可已把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会溢出
# 遗憾的是，大多数语言没有针对尾递归做优化，Python也没有做优化，即使换成尾递归的写法也会导致栈溢出
# 尾递归写法

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, result):
	if num == 1:
		return result
	return fact_iter(num-1, num * result)



