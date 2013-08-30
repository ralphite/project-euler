#!/usr/bin/env python

'''
p<=1000
a*a+b*b=(p-a-b)**2
a+b>p-a-b =>a+b>p/2
a>=b
a>p/4
'''
h={}
for p in range(3,1001):
    for a in range(p/4,p/2+1):
        for b in range(1,a+1):
            if a**2+b**2 == (p-a-b)**2:
                if not h.has_key(str(p)):
                    h[str(p)]=1
                else:
                    h[str(p)]+=1

p=0
v=0
for k in h.keys():
    if h[k]>v:
        v=h[k]
        p=k

print p
