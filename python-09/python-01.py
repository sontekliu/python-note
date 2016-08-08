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
	print f.read(); # 一次性读取文件全部内容

# 按行读取文件
with open('filetest.txt', 'r') as f:
	for line in f.readlines():
		print line ,

# 读取二进制文件        
with open('food.png', 'rb') as f:
	print f.read(10)

# 字符编码
with open('filetest2.txt', 'rb') as f:
	print f.read().decode('utf-8')

# 写文件（覆盖原有的内容）
with open('filetest2.txt', 'w') as f:
	f.write("abcd Hello World")



