#!/usr/bin/env python

p=1
for i in range(1,101):
    p*=i
print sum([int(i) for i in str(p)])
