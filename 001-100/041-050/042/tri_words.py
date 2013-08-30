#!/usr/bin/env python

a=open('words.txt').read().replace('"','').split(',')

tri=[i*(i+1)/2 for i in range(1,100)]

cnt=0
for w in a:
    if tri.count(sum([ord(c)-ord('A')+1 for c in w]))!=0:
        cnt+=1
print cnt
