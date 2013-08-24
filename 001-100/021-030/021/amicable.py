#!/usr/bin/env python

from math import sqrt

def gd(n):
    mid=int(sqrt(n))+1
    d=[1]
    for i in range(2,mid):
        if n%i==0:
            if d.count(i)==0:
                d.append(i)
            if d.count(n/i)==0:
                d.append(n/i)
    return d
a=[]
for i in range(1,10000):
    j=sum(gd(i))
    if sum(gd(j))==i and i!=j:
        a.append(i)

print sum(a)
