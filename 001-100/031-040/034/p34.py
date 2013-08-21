#!/usr/bin/env python

def f(n):
    assert n>=0
    p=1
    for i in range(2,n+1):
        p*=i
    return p

# obviously the special number is smaller than 1000000

a=[]

for i in range(3,1000000):
    if sum([f(int(j)) for j in str(i)])==i:
        a.append(i)

print sum(a)
