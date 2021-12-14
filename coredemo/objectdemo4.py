#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

print (re.match('www', 'www.googgle.com').span())  # 从起始位置匹配
print (re.match('com', 'www.google.com'))  # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group(): ", matchObj.group()
    print "matchObj.group(1): ", matchObj.group(1)
    print "matchObj.group(2): ", matchObj.group(2)
else:
    print "No match!!!"

# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group(): ", matchObj.group()
else:
    print "No match!!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print "search --> matchObj.group(): ", matchObj.group()
else:
    print "No match!!!"

'''
检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

语法：

re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的Python 注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是: ", num
