#!/usr/bin/env python

'''the number should be below 1mil because 9**5*7<1mil
'''

def f(n):
    r=0
    while n>0:
        d0=n%10
        r+=d0**5
        n=n/10
    return r

print sum([i for i in range(2,1000000) if f(i)==i])
