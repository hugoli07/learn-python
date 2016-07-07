# -*- coding: utf-8 -*-
# filter():内建函数，用于过滤序列

# 删除偶数
def is_odd(n):
	return n % 2 == 1
	
print filter(is_odd, [1, 2, 3, 4, 5, 7, 8])

# 删除序列中的空字符串
def not_empty(s):
	return s and s.strip()
	
print filter(not_empty, ['A', '', 'B', None, 'C', ' '])
