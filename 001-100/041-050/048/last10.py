#!/usr/bin/env python

def l10(k):
    r=1
    for i in range(0,k):
        r*=k
        r=r%(10**10)
    return r

s=0
for i in range(1,1001):
    s+=l10(i)

s=s%(10**10)

print s
