#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python While 循环语句
Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
while 判断条件：
    执行语句……
执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
当判断条件假false时，循环结束。
"""
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print "even is: ", even
print "odd is: ", odd

count = 0
while (count < 9):
    print 'The count is: ', count
    count = count + 1
print "Good bye!"

'''
while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：
'''
# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数 2 4 6 8 10
i = 1
while 1:
    print i  # 循环条件为1 必定成立
    i += 1  # 输出1 - 10
    if i > 10:  # 当 i 大于 10时跳出循环
        break

'''
无限循环
如果条件判断语句永远为 true，循环将会无限的执行下去，如下实例：
'''
# var = 1
# while var == 1:
#     num = raw_input("Enter a number: ")
#     print "You entered: ", num
# print "Good bye!"
# 注意：以上的无限循环你可以使用 CTRL+C 来中断循环。

"""
循环使用 else 语句
在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
"""
count = 0
while count < 5:
    print count, "is less than 5"
    count = count + 1
else:
    print count, "is not less than 5"

'''
简单语句组
类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
'''
# flag = 1
# while (flag): print "Given flag is really true!"
# print "Good bye!"
