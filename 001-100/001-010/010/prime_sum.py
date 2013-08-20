#!/usr/bin/env python
import sys,math
sys.path.append("../../../lib")
from natural import Prime

p = Prime()
s=0

while p.next()<math.sqrt(2000000):
    pass
pl = p.prime_list

s= sum(pl)

for i in range(pl[-1]+2,2000000,2):
    is_prime = True
    for j in pl:
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        s+=i

print s



