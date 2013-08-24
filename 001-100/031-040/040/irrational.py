#!/usr/bin/env python

n,i,a,b=0,1,[],[1,10,100,1000,10000,100000,1000000]
while n<=1000000:
    pn=n
    n+=len(str(i))
    for bb in b:
        bb=bb-1
        if pn<=bb and n>bb:
            a.append(str(i)[bb-pn])
    i+=1
p=1
for aa in a:
    p*=int(aa)

print p
