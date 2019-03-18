#!/usr/bin/python
# -*- coding:UTF-8 -*-
x = "a"
y = "b"
# 换行输出
print x
print y

print '---------------------'
# 不换行输出
print x,
print y,

# 不换行输出
print x, y

"""
多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
如下实例：
"""
expression = 1
if expression > 0:
    print ">"
elif expression == 0:
    print "="
else:
    print "<"
