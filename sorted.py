# -*- coding: utf-8 -*-
# 排序算法

print sorted([2, 32, 11, 8, 9])

def reverse_cmp(x, y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0
		
print sorted([2, 32, 11, 8, 9], reverse_cmp)

print sorted(['next', 'abs', 'Zoo', 'Credit'])

def cmp_ignore_case(s1, s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	elif u1 > u2:
		return 1
	else:
		return 0
print sorted(['next', 'abs', 'Zoo', 'Credit'], cmp_ignore_case)








