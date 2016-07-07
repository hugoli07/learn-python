# -*- coding: utf-8 -*-

def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print '2016-07-08'
	
f = now
print f()

# 函数对象有一个__name__属性，可以拿到函数的名称
print now.__name__
print f.__name__

