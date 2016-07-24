#!/usr/bin/python
# -*- coding:utf-8 -*-
# 迭代

L = ['sontek','jack','Bob','Sarch','Tracy']
for val in L:
    print val,

print ''
# dict 迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key,
print ''
for val in d.itervalues():
    print val,
print ''
for key, val in d.iteritems():
    print key, val

# string 迭代
for str in 'abcdefghijklmn':
    print str,
# 判断是否是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(123, Iterable)

    


