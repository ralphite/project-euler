#!/usr/bin/env python
import math

def defactor_count(n):
    mid = int(math.sqrt(n))
    count=0
    for i in range(1,mid+1):
        if n%i==0:
            count+=2
    if mid**2 == n:
        count-=1
    return count
i=0
while True:
    i=i+1
    if defactor_count(i*(i+1)/2)>500:
        print i*(i+1)/2
        break
