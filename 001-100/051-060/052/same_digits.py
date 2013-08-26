#!/usr/bin/env python

i=1
while True:
    i+=1
    s=set(str(i))
    if s==set(str(2*i)):
        if s==set(str(3*i)):
            if s==set(str(4*i)):
                if s==set(str(5*i)):
                    if s==set(str(6*i)):
                        print i
                        break
