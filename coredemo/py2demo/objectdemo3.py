#! /usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secreCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secreCount += 1
        self.publicCount += 1
        print self.__secreCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
# print counter.__secreCount  # 报错 实例不能访问私有变量
