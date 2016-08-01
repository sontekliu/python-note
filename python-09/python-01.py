#!/usr/bin/python
# -*- coding:utf-8 -*-

# 读取文件
f = open('filetest.txt', 'r')
print f.read()
f.close()

# try finally防止未关闭文件
try:
	f = open('filetest.txt', 'r')
	print f.read()
finally:
	if f:
		f.close()

# with语句不再调用close()方法
with open('filetest.txt', 'r') as f:
	print f.read();
