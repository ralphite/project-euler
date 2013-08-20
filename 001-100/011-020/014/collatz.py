#!/usr/bin/env python

h={}
h[1]=1
h[2]=2

def get_next(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

def get_seq_len(n):
    i=1
    t=n
    while t>1:
        if h.has_key(t):
            return h[t]+i-1
        t=get_next(t)
        i+=1
    return i

max=1

for i in range(3,1000000):
    h[i]=get_seq_len(i)
    if h[i]>h[max]:
        max=i

print max
