#!/usr/bin/python
#-*- coding:utf-8 -*-

# dict学习
# 1. dict 定义
d = {'micale': 90, 'bob':89, 'javaliu' : 99}
# 2. 判断是否在Key, key in d
print 'bob' in d

# 3. 取出key对应的值，若不存在返回None，第二个参数可指定不存在时的值
print d.get('bob')
print d.get('bobaaa', -1)

# 4. 显示dict
print d

# 5. 删除对应的key
d.pop('bob')

print d

# set 学习 set 是一组key的集合，但是key不能重复,只能放入不可变对象

# 1. set 定义

s = set([1,2,3,4])

print s

# 2. 添加元素
s.add(5)
print s

# 3. 删除元素

s.remove(4)
print s

s.add((1,2,3))
print s
s.add((1,2,[1,2]))   #放入不成功，set只能放入不可变对象
print s










