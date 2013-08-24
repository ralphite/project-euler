#!/usr/bin/env python

from datetime import datetime

cnt=0
for i in range(1901,2001):
    for j in range(1,13):
        if datetime(i,j,1).weekday()==6:
            cnt+=1
print cnt
