#!/usr/bin/env python

def cnr(n,r):
    assert n>=r
    assert n%1==0 and r%1==0
    if n-r<r:
        r=n-r
    pn=1
    for i in range(r):
        pn*=n-i
    for j in range(r):
        pn/=j+1
    return pn

c=0
for n in range(1,101):
    for r in range(1,n+1):
        if cnr(n,r)>10**6:
            c+=1
print c
