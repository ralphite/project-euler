#!/usr/bin/env python

p=[]
for a in range(1,5000):
    for b in range(1,5001):
        if a>b:
            continue
        c=a*b
        if len(str(a)+str(b)+str(c))>9:
            continue
        l=[int(ca) for ca in str(a)] + \
                [int(cb) for cb in str(b)] + \
                [int(cc) for cc in str(c)]
        l.sort()
        if len(l)==9 and l==[1,2,3,4,5,6,7,8,9]:
            print a,b,c
            if not c in p:
                p.append(c)
print
print sum(p)
