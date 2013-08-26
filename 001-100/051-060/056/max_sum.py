#!/usr/bin/env python
arr=[]
for s in [str(a**b) for a in range(1,100) for b in range(1,100)]:
    arr.append(sum([int(c) for c in s]))
print max(arr)
