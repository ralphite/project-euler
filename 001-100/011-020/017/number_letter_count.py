#!/usr/bin/env python

def digi2eng(n):
    assert(n>0 and n<1001)
    if n==1:
        return 'one'
    if n==2:
        return 'two'
    if n==3:
        return 'three'
    if n==4:
        return 'four'
    if n==5:
        return 'five'
    if n==6:
        return 'six'
    if n==7:
        return 'seven'
    if n==8:
        return 'eight'
    if n==9:
        return 'nine'
    if n==10:
        return 'ten'
    if n==11:
        return 'eleven'
    if n==12:
        return 'twelve'
    if n==13:
        return 'thirteen'
    if n==14:
        return 'fourteen'
    if n==15:
        return 'fifteen'
    if n==16:
        return 'sixteen'
    if n==17:
        return 'seventeen'
    if n==18:
        return 'eighteen'
    if n==19:
        return 'nineteen'
    if n==20:
        return 'twenty'
    if n==30:
        return 'thirty'
    if n==40:
        return 'forty'
    if n==50:
        return 'fifty'
    if n==60:
        return 'sixty'
    if n==70:
        return 'seventy'
    if n==80:
        return 'eighty'
    if n==90:
        return 'ninety'
    if n>20 and n<100:
        return digi2eng((n/10)*10)+'-'+digi2eng(n%10)
    if n>99 and n<1000 and n%100==0:
        return digi2eng(n/100)+' hundred'
    if n>99 and n<1000 and n%100!=0:
        return digi2eng(n/100)+' hundred and '+digi2eng(n%100)
    if n==1000:
        return 'one thousand'

print sum([len(digi2eng(i).replace(' ','').replace('-','')) for i in range(1,1001)])
