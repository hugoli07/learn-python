# -*- coding: utf-8 -*-
# 列表生成式：list comprehensions，创建list

print range(1, 11)


print "生成[1*1, 2*2, 3*3,..., 10*10]列表：", [x * x for x in range(1, 11)]

print [y * y for y in range(1, 11) if y % 2 == 0]

# 两层循环生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 运用列表生成式，列出当前目录所有文件
import os
print [d for d in os.listdir('.')]

# 列表生成式可以使用两个变量来生成list
d = {'X': 'A', 'Y': 'B', 'Z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]

# 将所有字符串小写
print [s.lower() for s in d]
