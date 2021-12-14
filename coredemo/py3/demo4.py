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

if a > b:
    print("4-a大于b")
else:
    print("4-a小于等于b")

# 修改变量a 和 b的值
a = 5
b = 20
if a <= b:
    print("5-a小于等于b")
else:
    print("5-a大于b")

if b >= a:
    print("6-b大于等于a")
else:
    print("6-b小于a")

# Python赋值运算符

a = 21
b = 10
c = 0

c = a + b
print("1-c的值为：", c)

c += a
print("2-c的值为: ", c)

c *= a
print("3-c的值为: ", c)

c /= a
print("4-c的值为: ", c)

c = 2
c %= a
print("5-c的值为: ", c)

c **= a
print("6-c的值为: ", c)

c //= a
print("7-c的值为: ", c)

# Python 位运算符
a = 60
b = 13
c = 0

c = a & b
print("1-c的值为: ", c)

c = a | b
print("2-c的值为: ", c)

c = a ^ b
print("3-c的值为: ", c)

c = ~a
print("4-c的值为: ", c)

c = a << 2
print("5-c的值为: ", c)

c = a >> 2
print("6-c的值为: ", c)

# Python 逻辑运算符
a = 10
b = 20

if a and b:
    print("1-变量a和b都为true")
else:
    print("1-变量a和b有一个不为true")

if a or b:
    print("2-变量a和b都为true,或其中一个变量为true")
else:
    print("2-变量a和b都不为true")

# 修改变量a的值
a = 0
if a and b:
    print("3-变量a和b都为true")
else:
    print("3-变量a和b有一个不为true")

if a or b:
    print("4-变量a和b都为true，或其中一个变量为true")
else:
    print("4-变量a和b都不为true")

if not (a and b):
    print("5-变量a和b都为false,或其中一个变量为false")
else:
    print("5-变量a和b都为true")

# Python成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("1-变量a在给定的列表list中")
else:
    print("1-变量a不在给定的列表list中")

if (b not in list):
    print("2-变量b不在给定的列表list中")
else:
    print("2-变量b在给定的列表list中")

# 修改变量a的值
a = 2
if (a in list):
    print("3-变量a在给定的列表list中")
else:
    print("3-变量a不在给定的列表list中")

# Python身份运算符
a = 20
b = 20

if a is b:
    print("1-a和b有相同的标识")
else:
    print("1-a和b没有相同的标识")

if (id(a) == id(b)):
    print("2-a和b有相同的标识")
else:
    print("2-a和b没有相同的标识")

# 修改变量b的值
b = 30
if a is b:
    print("3-a和b有相同的标识")
else:
    print("3-a和b没有相同的标识")

if (a is not b):
    print("4-a和b没有相同的标识")
else:
    print("4-a和b有相同的标识")