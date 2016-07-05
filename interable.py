# -*- coding: utf-8 -*-
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历称为迭代(Iteration)

d = {'a': 1, 'b': 2, 'c': 3}
# 迭代key
for key in d:
	print key
	
#迭代value
for value in d.itervalues():
	print value
	
# 迭代key和value
for k, v in d.iteritems():
	print k, v
	
# 迭代字符串
for ch in 'ABC':
	print ch
	
	
# 判断一个对象是否可以迭代
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1, 2, 3], Iterable)
isinstance(123, Iterable)

# for循环中同时引入两个变量
for x, y in [(1, 1), (2, 2), (3, 3)]:
	print x, y
	

