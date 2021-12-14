#!/usr/bin/python3

# Python3 基础语法
# 数字(Number)类型
'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

# 字符串(String)
'''
python中单引号和双引号使用完全相同。
使用三引号(\''' 或 """)可以指定一个多行字符串。
转义符 \
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''
str = '123456789'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str * 2)
print(str + '你好')

# 等待用户输入
# input("\n\n按下 enter 键后退出。")

# 同一行显示多条语句
import sys;

x = 'hello';
sys.stdout.write(x + '\n')

# print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('--------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()
