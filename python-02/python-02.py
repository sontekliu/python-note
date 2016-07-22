#!/usr/bin/python
# -*- coding:utf-8 -*-

# 1. 函数定义 def语句，依次写出函数名、括号、括号中的参数和冒号:

def my_fun(x):
	temp = int(x)
	if(temp>0):
		print temp
	else:
		print "This is a fushu"
		
my_fun(3)

# 2. 空函数
def fun_none():
	pass

# 3. 参数检查
def param_check(x):
	if not isinstance(x, (int, float)):
		# 抛出错误提示
		raise TypeError('Bad operand type')
	else:
		print x

# 若要运行下面代码，请把下面一行代码注释掉即可
param_check('A')
# 上面代码报错，下面代码不会执行
param_check(4444)

# 4. 返回多个值,其实真正返回的是tuple，只是省略了括号

def mult_value(x, y):
	return x, y

print mult_value(5,23)

a, b = mult_value(3,4)
print a, b



