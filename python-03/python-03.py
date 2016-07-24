#!/usr/bin/python
# -*- coding:utf-8 -*-

# 列表生成式，用来快速生成list

print range(1,10)

print [x*x for x in range(1,11)]

print [x*x for x in range(1,11) if x % 2 ==0 ]

import os
print [d for d in os.listdir('.')]

lis = ['Hello', 2, 'ABC', 'Zhangbo', None]
print [s.lower() for s in lis if isinstance(s, str)]






