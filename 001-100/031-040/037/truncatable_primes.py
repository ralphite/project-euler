#!/usr/bin/env python

from math import sqrt

def isp(n):
    assert n%1==0 and n>=1
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

assert [2,3,5,7,11,13,17,19]==[i for i in range(2,20) if isp(i)]

def f(n):
    s=str(n)
    a=[s[:i] for i in range(1,len(s))]+[s[i:] for i in range(1,len(s))]+[s]
    a=[int(i) for i in a]
    a.sort()
    for i in a:
        if not isp(i):
            return False
    return True

cnt=0

i=23
a=[]
while cnt<11:
    if f(i):
        cnt+=1
        a.append(i)
    i+=2

print sum(a)
