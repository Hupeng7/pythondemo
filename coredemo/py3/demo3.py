#!/usr/bin/python3

# Python3基本数据类型

counter = 100
miles = 1000.0
name = "bruce"

print(counter)
print(miles)
print(name)

'''
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
'''
list = ['abcd', 789, 2.23, 'bruce', 70.2]
tinylist = [123, 'bruce']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
'''
tuple = ('abcd', 786, 2.23, 'bruce', 70.2)
tinytuple = (123, 'bruce')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

'''
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
print(sites)

# 成员测试
if 'Runoob' in sites:
    print('Runoob in the Set')
else:
    print('Runoob not in Set')

# set可以进行稽核运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

'''
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。

另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
注意：
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
'''
dict = {}
dict['one'] = "1 - 教程"
dict[2] = "2 - 工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict)
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())























