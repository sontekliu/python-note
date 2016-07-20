#!/usr/bin/python
#-*- coding:utf-8 -*-

''' 关于编码问题
	最早的计算机采用8个比特(bit)作为一个字节(byte)

	ASCII 编码: 只有127个字母，大小写英文字母，数字，特殊符号。，比如:A的编码是65
	GB2312编码: 为了不和ASCII冲突，又能把中文编进去，中国制定了GB2312编码 需要两个字节才能把中文编进去.
	其他编码:Shift_JIS,日本编码，Euc-kr,韩国编码，各国有各国的标准，难免会出现冲突，所以出现了乱码
	Unicode编码: 把所有语言都统一到一套编码里，为了适应各种语言，使用两个字节表示一个字符，特殊字符可能需要4个字节
				如果文本内容基本全是英文的话，Unicode编码要比ASCII编码要多一倍的存储空间，在存储和传输上不划算
	可变长编码:UTF-8'''

print ord('A')
print chr(65)

for i in range(257):
	print i , '-->', chr(i),

print 
print u'中文'.encode('utf-8')


