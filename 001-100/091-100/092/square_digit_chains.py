#!/usr/bin/env python

def f(n):
    r=0
    while n>0:
        r+=(n%10)**2
        n/=10
    return r

h={}
for i in range(1,10000000+1):
    s=f(i)
    if not h.has_key(s):
        h[s]=1
    else:
        h[s]+=1

s=0

def g(n):
    while n!=1 and n!=89:
        n=f(n)
    return n==89

for k in h.keys():
    if g(k):
        s+=h[k]

print s
