#!/usr/bin/env python
import sys
sys.path.append("../../../lib")
from natural import Prime

p = Prime()
for i in range(1,10001):
    p.next()
print p.next()
