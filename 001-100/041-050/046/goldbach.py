#!/usr/bin/env python

from math import sqrt

def isp(n):
    assert n%1==0
    if n<=1 or n==4:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

assert [i for i in range(1,20) if isp(i)]==[2,3,5,7,11,13,17,19]

def f(n):
    for i in range(1,int(sqrt(n/2))+1):
        if isp(n-i**2*2):
            return False
    return True

i=9
while True:
    if (not isp(i)) and f(i):
        print i
        break
    i+=2
