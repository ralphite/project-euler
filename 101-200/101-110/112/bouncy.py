#!/usr/bin/env python

def is_b(n):
    assert n%1==0 and n>0
    if n<100:
        return False
    a=[]
    while n>0:
        a.append(n%10)
        n/=10
    if (a[0]-a[1])*(a[1]-a[2])<0:
        return True
    b=[a[0]]
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            b.append(a[i])
    if len(b)==1:
        return False
    if b[0]>b[1]:
        b=[9-i for i in b]
    for i in range(0,len(b)-1):
        if b[i]>b[i+1]:
            return True
    return False

assert sum([1 for i in range(1,21781) if is_b(i)])/21780.0 == 0.9

i,b=1,0
while True:
    if is_b(i):
        b+=1
    if b*1.0/i==0.99:
        print i
        break
    i+=1
