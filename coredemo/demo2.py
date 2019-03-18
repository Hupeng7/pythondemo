#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
Python 变量类型
变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
"""
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "Leo"  # 字符串
print counter
print miles
print name

# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print a, b, c
a, b, c = 1, 2, "john"
print a, b, c

"""
标准数据类型
在内存中存储的数据可以有多种类型。
例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""

'''
Python数字
数字数据类型用于存储数值。

他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。

当你指定一个值时，Number对象就会被创建：

var1 = 1
var2 = 10
您也可以使用del语句删除一些对象的引用。

del语句的语法是：

del var1[,var2[,var3[....,varN]]]]
您可以通过使用del语句删除单个或多个对象的引用。例如：

del var
del var_a, var_b
'''

"""
Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
"""

'''
Python字符串
字符串或串(String)是由数字、字母、下划线组成的一串字符。

一般记为 :

s="a1a2···an"(n>=0)
它是编程语言中表示文本的数据类型。

python的字串列表有2种取值顺序:

从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
'''
str = "Hello World!"
print str       # 输出完整字符串
print str[0]    # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]   # 输出从第三个字符串开始的字符串
print str * 2   # 输出字符串两次
print str + "TEST"  # 输出连接的字符串















