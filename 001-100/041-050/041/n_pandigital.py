#!/usr/bin/env python

from math import sqrt

# only with 1/4/7 digits, otherwise divisable by 3

def is_prime(n):
    assert n>1 and n%1==0
    if n==2 or n==3:
        return True
    if n==4:
        return False
    mid = int(sqrt(n))+2
    if n%2==0:
        return False
    for i in range(3,mid,2):
        if n%i ==0:
            return False
    return True


for i in range(7654321,0,-1):
    if set([int(c) for c in str(i)])==set([j for j in range(1,len(str(i))+1)]):
        if is_prime(i):
            print i
            break
