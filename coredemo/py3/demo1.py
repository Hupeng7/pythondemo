#!/usr/bin/python3

'''
注释
Python中单行注释以 # 开头，

多行注释可以用多个 # 号，还有 \''' 和 """：
'''

# 第一个注释
print("Hello,Python!")  # 第二个注释

# 第一个注释
# 第二个注释

'''
第三个注释
第四个注释
'''

"""
第五个注释
第六个注释
"""

print("Hello,Python!again")

'''
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
'''
if True:
    print("True")
else:
    print("False")

'''
多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
'''
item_one = 'a'
item_two = 'b'
item_three = 'c'
total = item_one + \
        item_two + \
        item_three
print(total)
