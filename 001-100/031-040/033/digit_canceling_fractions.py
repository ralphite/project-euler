#!/usr/bin/env python
p=[1,1]
for i,j in [(i,j) for i in range(10,100) if i%10!=0 for j in range(10,100) if j%10!=0 and i<j and (i/10==j/10 or i/10==j%10 or i%10==j/10 or i%10==j%10)]:
    if i/10==j/10:
        if (i%10)*j==i*(j%10):
            p[0]*=i
            p[1]*=j
    if i/10==j%10:
        if (i%10)*j==i*(j/10):
            p[0]*=i
            p[1]*=j
    if i%10==j%10:
        if (i/10)*j==i*(j/10):
            p[0]*=i
            p[1]*=j
    if i%10==j/10:
        if (i/10)*j==i*(j%10):
            p[0]*=i
            p[1]*=j

print p[1]*1./p[0]
