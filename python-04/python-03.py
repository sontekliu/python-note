#!/usr/bin/python
# -*- coding:utf-8 -*-

# filter 函数
# filter 接收一个函数和一个序列，和map不同的是，filter把传入的函数依次作用于每个元素，然后根据返回值
# 是True还是False决定保留还是丢弃该元素
def is_odd(n):
	return n % 2 == 1
print filter(is_odd, [1,2,3,4,5,6,7,8,9])

