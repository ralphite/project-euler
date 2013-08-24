#!/usr/bin/env python

s=open('names.txt').read()
s=s.replace('"','')
a=s.split(',')
a.sort()

print sum([sum([ord(c)-ord('A')+1 for c in a[i]])*(i+1) for i in range(0,len(a))])
