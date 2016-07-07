# -*- coding: utf-8 -*-

# 直接求和
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
	
print calc_sum(1, 2, 3)


# 根据需要求和
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
	
f = lazy_sum(1, 3, 5, 7, 9)
print f()
