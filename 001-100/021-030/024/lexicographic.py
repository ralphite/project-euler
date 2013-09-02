#!/usr/bin/env python
def f(n):
    p=1
    for i in range(2,n+1):
        p*=i
    return p

def g(n):
    if n==0:
        return []
    a=[]
    for i in range(9,-1,-1):
        j=0
        while f(i)*j<=n:
            j+=1
        n=n-f(i)*(j-1)
        a.append(j-1)
    return a
a=g(999999)
b=list(range(0,10))
c=[]
for i in a:
    c.append(b[i])
    b.remove(b[i])

print ''.join([str(i) for i in c])
