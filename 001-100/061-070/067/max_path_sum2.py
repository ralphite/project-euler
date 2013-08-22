#!/usr/bin/env python

s=open('triangle.txt').read()
a=[i.split() for i in s.strip().split('\n')]

def f(a,b):
    return [max([a[i]+b[i], a[i]+b[i+1]]) for i in range(0,len(a))]

m=[0 for i in range(0,len(a[-1])+1)]

for i in range(len(a)-1,-1,-1):
    m=f([int(j) for j in a[i]],m)


assert len(m)==1
print m[0]
