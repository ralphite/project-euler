#!/usr/bin/env python

'''a+2b+5c+10d+20e+50f+100g+200h=200'''

'''200*100*40*20*10*4*2*1>1b'''
cnt=0
for h in [1,0]:
    for g in range((200-200*h)/100, -1, -1):
        for f in range((200-200*h-100*g)/50, -1, -1):
            for e in range((200-200*h-100*g-50*f)/20, -1, -1):
                for d in range((200-200*h-100*g-50*f-20*e)/10, -1, -1):
                    for c in range((200-200*h-100*g-50*f-20*e-10*d)/5, -1, -1):
                        for b in range((200-200*h-100*g-50*f-20*e-10*d-5*c)/2, -1, -1):
                            for a in range(200-200*h-100*g-50*f-20*e-10*d-5*c-2*b, -1, -1):
                                if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h==200:
                                    cnt+=1

print cnt
