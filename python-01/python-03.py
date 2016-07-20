#!/usr/bin/python
#-*- coding:utf-8 -*-

# tuple 不可变
t1 = (1,2,"a",True,False);
# list 可变
t2 = [1,2,"a",True,False];

print (t1, type(t1))
print (t2, type(t2))

# [下限:上限:步长]  不包括上限
print t1[0:3:2]

# 将序列翻转
print t2[::-1] 

# 添加元素
t2.append('aaa')
print t2
# 指定位置添加元素
t2.insert(1,'1111')
print t2
# 修改元素
t2[1] = "abc"
# 删除元素
t2.pop()
print t2
t2.pop(3)
print t2
