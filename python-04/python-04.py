#!/usr/bin/python
# -*- coding:utf-8 -*-

# sorted 函数
# 1. sorted函数对list进行排序
print sorted([1,3,-12,34,22,89])

# 2. 接收一个key函数来实现自定义排序
print sorted([1,3,-12,34,22,89], key=abs)

# 3. 正序或者到序排序序列
print sorted([1,3,-12,34,22,89], key=abs, reverse=True)

# 练习 将下列列表用name或者score排序
L = [('Bob', 75),('Adam', 92),('Bart', 66), ('Lisa', 88)]
def by_name(x, y):
	return x

def by_score(x, y):
	return y
print sorted(L, key=lambda x: x[0])
print sorted(L, key=lambda x: x[1])






