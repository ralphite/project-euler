#!/usr/bin/env python
h={}
def p(n,m):
    if h.has_key((n,m)):
        return h[(n,m)]
    if n==1 or m==1:
        h[(n,m)]=1
        return 1
    h[(n,m)]=p(n-1,m)+p(n,m-1)
    return h[(n,m)]

print p(21,21)
