#!/usr/bin/env python

print [i*j*(1000-j-i) for i in range(1,1000) for j in range(1,i) if i*i+j*j==(1000-i-j)**2][0]
