#!/usr/bin/python
#-*- coding:utf-8 -*-

# dict学习
# 1. dict 定义
d = {'micale': 90, 'bob':89, 'javaliu' : 99}
# 判断是否在Key
# key in d
print 'bob' in d

# 取出key对应的值，若不存在返回None，第二个参数可指定不存在时的值
print d.get('bob')
print d.get('bobaaa', -1)



