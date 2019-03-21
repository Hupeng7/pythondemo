#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python for 循环语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

语法：

for循环的语法格式如下：

for iterating_var in sequence:
   statements(s)
"""
for letter in 'Python':
    print '当前字母: ', letter
print "spell Python done!"

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print "当前水果: ", fruit
print "Good bye!"

# 以上实例我们使用了内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。

'''
循环使用 else 语句
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
'''
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print "%d 等于 %d * %d " % (num, i, j)
            break
    else:
        print num, "是一个质数"

"""
Python 循环嵌套
Python 语言允许在一个循环体里面嵌入另一个循环。

Python for 循环嵌套语法：

for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
Python while 循环嵌套语法：

while expression:
   while expression:
      statement(s)
   statement(s)
你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。
"""
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, "是素数"
    i = i + 1
print "Good bye!"

"""
Python break 语句
Python break语句，就像在C语言中，打破了最小封闭for或while循环。

break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

break语句用在while和for循环中。

如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

Python语言 break 语句语法：

break
"""
for letter in 'Python':
    if letter == 'h':
        break
    print "当前字母： ", letter

var = 10
while var > 0:
    print "当前变量值： ", var
    var = var - 1
    if var == 5:
        break
print "Good bye!"

"""
Python continue 语句
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
Python 语言 continue 语句语法格式如下：
continue
"""
for letter in "Python":
    if letter == 'h':
        continue
    print "当前字母： ", letter
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print "当前变量值： ", var
print "Good bye!"

# continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
var = 10
while var > 0:
    var = var - 1
    if var == 5 or var == 8:
        continue
    print "当前值： ", var
print "Good bye!"

# 我们想只打印0-10之间的奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print (n)
print "done!"
