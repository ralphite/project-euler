#!/usr/bin/env python
from math import sqrt

def is_p(h):
    '''n=1/6+-sqrt(2h/3+1/36)'''
    return (1+sqrt(24*h+1))%6==0

def is_t(h):
    '''n=+-sqrt(2h+1/4)-1/2'''
    return (sqrt(8*h+1)-1)%2==0

n=0
while True:
    n+=1
    h=n*(2*n-1)
    if is_p(h) and is_t(h) and h>40755:
        print h
        break
