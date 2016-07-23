#!/usr/bin/python
# -*- coding:utf-8 -*-
# 切片

L = ['sontek','jack','Bob','Sarch','Tracy']

print L[0:3]
print L[:3]

L = range(100)
# 取前10个元素
print L[:10]
# 取后10个元素
print L[-10:]
# 前10个元素，每隔2个取一个
print L[:10:2]
# 复制一个list
print L[:]

# tuple 和 list类似不再举例
# string 截取，string有了切片操作，可以省略好多截取函数
print 'ABCDEFGHIJKLMN'[:3]
print 'ABCDEFGHIJKLMN'[::2]



















