#!/usr/bin/env python
from math import log

s=open('base_exp.txt').read().split('\n')
a=[i.split(',') for i in s]
a=[(int(i[0]),int(i[1])) for i in a]
a=[i[1]*log(i[0]) for i in a]

print a.index(max(a))+1
