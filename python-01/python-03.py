#!/usr/bin/python
#-*- coding:utf-8 -*-

t1 = (1,2,"a",True,False);
t2 = [1,2,"a",True,False];

print (t1, type(t1))
print (t2, type(t2))

# [下限:上限:步长]  不包括上限
print t1[0:3:2]

# 将序列翻转
print t2[::-1] 
