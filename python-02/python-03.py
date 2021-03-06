#!/usr/bin/python
# -*- coding:utf-8 -*-

# 函数不同参数讲解，默认参数、可变参数、关键字参数

# 1. 默认参数

def power(x, n=2):
	s = 1
	while n>0:
		n = n - 1
		s = s * x
	return s

print power(4,2)

def student(name, gender, age=23, city='beijing'):
	print name, gender, age, city
print ''

student('lily', 'M')
student('lily', 'M', 24)
student('lily', 'M', city='shanghai')
# 总结，比选参数在前，默认参数在后，如果不是按照顺序提供默认参数时，需要把参数名写上
# 默认参数陷阱
def add_end(L = []):
	L.append('END')
	return L

print add_end() # 输出 ['END']
print add_end() # 输出 ['END','END']
# 解释原因，Python在定义的时候，默认参数L就被计算出来了，L是变量，指向[]，每次调用函数改变了L的内容，
# 下次调用时，默认参数的内容就变了。所以，定义默认参数必须指向不变对象
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L


# 2. 可变参数，顾名思义，就是参数个数是可以变化的，可以是1个，2个到任意个，还可以是0个

def list_sum(numbers):
	sum_val = 0
	for n in numbers:
		sum_val = sum_val + n
	return sum_val
# 考虑使用list或者tuple作为参数值
print list_sum([1,2,3,4])

# 改为可变参数如下
def list_sum(*numbers):
	sum_val = 0
	for n in numbers:
		sum_val = sum_val + n
	return sum_val

# 使用可变参数的函数，传递参数时，不需要list或者tuple
print list_sum(1,2,3)
# 使用可变参数的函数，如果传递的是list或者tuple时
nums = [1,2,3,4,5]
print list_sum(nums[0],nums[1],nums[2],nums[3],nums[4])
# 或者
print list_sum(*nums) # 常用

# 3. 关键字参数，关键字参数允许你传入0个或者任意含参数名的参数，这些关键字在函数内部自动组装成为一个dict

def show(name, age, **kv):
	print 'name:', name, 'age:', age, 'other:', kv

show('zhangsan', 30)
show('zhangsan', 30, city='beijing', gender="M")

kv = {'city':'beijing','gender':'M'}
show('zhangs',33, **kv)

# 4. 组合参数，即，必选参数、默认参数、可变参数和关键字参数组合使用，
# 参数定义的顺序必须是:必选参数、默认参数、可变参数和关键字参数

def fun(x, y=10, z=20, *args, **kv):
	print 'x=', x, 'y=', y, 'z=', z, 'args=', args, 'kv', kv

fun('A')
fun('A', 23)
fun('A', 23, 1, 2, 3, 4)
fun('A', 23, 1, 2, 3, 4, c='v')
lll = [1, 3, 4, 5]
kv = {'abc':'xyz'}
fun(*lll, **kv)

# 总结，对于任意函数，都可有使用fun(*args, **kv)的形式调用它，无论其参数是如何调用的




