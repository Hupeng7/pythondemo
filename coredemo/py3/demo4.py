#!/usr/bin/python3

# Python算术运算符
a = 21
b = 10
c = 0

c = a + b
print("1-c的值为：", c)

c = a - b
print("2-c的值为: ", c)

c = a * b
print("3-c的值为: ", c)

c = a / b
print("4-c的值为: ", c)

c = a % b
print("5-c的值为: ", c)

# 修改变量 a b c
a = 2
b = 3
c = a ** b
print("6-c的值为: ", c)

a = 10
b = 5
c = a // b
print("7-c的值为：", c)

# Python比较运算符
a = 21
b = 10
c = 0
if a == b:
    print("1-a等于b")
else:
    print("1-a不等于b")

if a != b:
    print("2-a不等于b")
else:
    print("2-a等于b")

if a < b:
    print("3-a小于b")
else:
    print("3-a大于等于b")
