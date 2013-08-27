#!/usr/bin/env python

"""
for p in prime_list_under_1M:
    if p has an even digit:
        go to next p
    for i in get_all_circular_numbers(p):
        if not is_prime(i):
            go to next p
    p is a circular prime
"""
from math import sqrt

def isp(n):
    assert(n>0)
    assert(n%1==0)
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def no_even_d(n):
    for c in str(n):
        if int(c)%2==0:
            return False
    return True
a=[2]
for i in range(1,1000000):
    if isp(i):
        if no_even_d(i):
            found=True
            for j in range(0,len(str(i))):
                if not isp(int(str(i)[j:]+str(i)[:j])):
                    found = False
            if found:
                a.append(i)

print len(a)
