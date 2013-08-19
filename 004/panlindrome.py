#!/usr/bin/env python

print max([k for k in [i*j for i in range(990,100,-11) for j in range(999,99,-1) if i*j%10!=0] if str(k)[::-1]==str(k)])
