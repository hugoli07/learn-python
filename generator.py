# -*- coding: utf-8 -*-
# 边循环边计算的机制，称为生成器(generator)

g = (x * x for x in range(10))
g

print g.next()
print g.next()
print g.next()

for n in g:
	print n
	
	
# Fibonacci斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a +b
		n = n + 1
		
print fib(5)
