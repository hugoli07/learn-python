# -*- coding: utf-8 -*-
# list

# 定义list
classmates = ['Michael', 'Bob', 'Tracy']
# 显示list内容
print classmates

# 获取classmates中元素个数
print len(classmates)

# 用索引访问list中每个位置的元素
print classmates[0]
print classmates[1]
print classmates[2]
print classmates[-1]
print classmates[-2]
print classmates[-3]

# 往list中追加元素到末尾
classmates.append('Adam')
print classmates

# 把元素插入到指定位置
classmates.insert(1, 'Jack')
print classmates

# 删除list末尾的元素
classmates.pop()
print classmates

# 删除指定位置的元素，pop(i)
classmates.pop(1)
print classmates

# 元素替换，直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print classmates

# list中元素的数据类型可以不同
L = ['Apple', 123, True]
print L

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)
print s
print s[2][1]

# 空list
L = []
print len(L)

