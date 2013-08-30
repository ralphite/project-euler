#!/usr/bin/env python

'''obviously b is a prime
1+a+b is also prime
and 4+2a+b
so 3+a is even, then a is odd'''

from math import sqrt

def isp(n):
    assert n%1==0
    if n<=1:
        return False
    if n<4:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def get_l(a,b):
    if not isp(b):
        return 0
    l=1
    for i in range(1,b):
        if isp(i*i+a*i+b):
            l+=1
        else:
            break
    return l

assert get_l(1,41)==40

bl=[i for i in range(1,1000) if isp(i)]

h={'a':0, 'b':0, 'length':0}

for b in bl:
    for a in range(1,1000):
        l=get_l(a,b)
        if h['length']<l:
            h['length']=l
            h['a']=a
            h['b']=b
        l=get_l(-a,b)
        if h['length']<l:
            h['length']=l
            h['a']=-a
            h['b']=b

print h['a']*h['b']
