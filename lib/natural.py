#!/usr/bin/env python

import math

class Prime():
    def __init__(self):
        self.prime_list=[]
    def next(self):
        if len(self.prime_list)==0:
            self.prime_list.append(2)
            return 2
        if self.prime_list[-1]==2:
            self.prime_list.append(3)
            return 3
        check_number = self.prime_list[-1] + 2
        is_prime = False
        while True:
            mid = int(math.sqrt(check_number)) + 1
            for i in range(0,len(self.prime_list)):
                if self.prime_list[i] >= mid:
                    is_prime = True
                    break
                if check_number % self.prime_list[i] == 0:
                    break
            if is_prime:
                self.prime_list.append(check_number)
                break
            check_number += 2
        return check_number


def defactor(n):
    assert n%1==0
    assert n>0
    if n==1:
        return [1]
    if n<4:
        return [1,n]
    mid = int(math.sqrt(n)) + 1
    p = Prime()
    a=[1]
    k = p.next()
    while k<mid:
        if n%k==0:
            a.append(k)
            a.append(n/k)
        k = p.next()
    a.sort()
    return a

if __name__ == "__main__":
    p = Prime()
    for i in range(10):
        print p.next(),
    print defactor(21)
