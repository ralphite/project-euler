#!/usr/bin/env python

'''
when n=2
a<=9999 and 2a>=10000

when n=3
100<=a<=999

when n=4
10<=3a<=99 and 4a>=100

when n=5
1<=a<=9 2a>=10

...

when n=9
a=1
'''

def f(a_min, a_max, n):
    r=[]
    for a in range(a_min,a_max+1):
        s=''.join([str(a*i) for i in range(1,n+1)])
        if len(s)==9 and set([c for c in s])==set([str(i) for i in range(1,10)]):
            r.append(int(s))
    return r

print max(f(1,1,9)+f(1,9,8)+f(1,9,7)+f(1,9,6)+f(1,9,5)+f(25,33,4)+f(100,999,3)+f(5000,9999,2))
