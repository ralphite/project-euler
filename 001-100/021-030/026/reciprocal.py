#!/usr/bin/env python

def f(n):
    assert n%1==0 and n>1 and n<1000
    dl,ul=[],[]
    u=1
    while True:
        u*=10
        u=u%n
        repeat=0
        if ul.count(u)==0:
            ul.append(u)
        else:
            repeat=u
            break
        if u==0:
            return 0
    return len(ul)-ul.index(repeat)

l,n=0,0
for i in range(2,1000):
    if f(i)>l:
        l=f(i)
        n=i
print n
