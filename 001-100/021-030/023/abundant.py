#!/usr/bin/env python
from math import sqrt

def is_abundant(n):
    assert n%1==0
    if n==1:
        return False
    a=[1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            if a.count(i)==0:
                a.append(i)
            if a.count(n/i)==0:
                a.append(n/i)
    return sum(a)>n

def is_sum_abu(n):
    for i in range(1,int(n/2)+1):
        if is_abundant(i) and is_abundant(n-i):
            return True
    return False

s=sum(range(1,24))
for i in range(24, 28124):
    if not is_sum_abu(i):
        s+=i

print s
