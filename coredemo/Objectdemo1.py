#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary


"创建Employee类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建Employee类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7
print hasattr(emp1, 'age')
emp1.age = 8
print getattr(emp1, 'age')
del emp1.age
print hasattr(emp1, 'age')

setattr(emp1, 'age', 8)
print getattr(emp1, 'age')
delattr(emp1, 'age')
print hasattr(emp1, 'age')

'''
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
Python内置类属性调用实例如下：
'''
print "Employee.__doc__: ", Employee.__doc__
print "Employee.__name__: ", Employee.__name__
print "Employee.__module__: ", Employee.__module__
print "Employee.__bases__: ", Employee.__bases__
print "Employee.__dict__: ", Employee.__dict__
