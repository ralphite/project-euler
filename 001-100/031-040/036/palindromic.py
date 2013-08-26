#!/usr/bin/env python

def is_p(n):
    s=str(n)
    return s==s[::-1]

def b(n):
    return bin(n)[2:]
s=0
for i in range(1,1000000):
    if is_p(i):
        if is_p(b(i)):
            s+=i
print s
