#!/usr/bin/env python

import math

n = 600851475143

a = [i for i in range(3,int(math.sqrt(n))+1,2) if n%i==0]

for i in a:
    for j in a:
        if j>i and j%i==0:
            a.remove(j)

print a[-1]
