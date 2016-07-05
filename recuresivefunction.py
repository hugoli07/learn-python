# -*- coding: utf-8 -*-
# 递归函数（recursive function）

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
	
print fact(1)
print fact(5)
print fact(100)

# 尾递归：在函数返回时，调用函数本身，并且，return语句不能包含表达式。这样
# 编译器或者解释器就可以把尾递归做优化，使递归本身无论用多少次，都只占用
# 一个栈帧，不会出现栈溢出的情况

def fact2(n):
	return fact2_iter(n, 1)
	
def fact2_iter(num, product):
	if num == 1:
		return product
	return fact2_iter(num - 1, num * product)
	