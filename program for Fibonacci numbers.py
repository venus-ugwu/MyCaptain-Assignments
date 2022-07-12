# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:34:43 2022

@author: venus
"""

#note to captain: is it possible for you to send me your email through the feedback form? 
#as i would like to ask you a few questions on work experience.

print("program for Fibonacci numbers")

numrange = int(input("Please input how many values you want printed:"))

value1 = 0
value2 = 1

for n in range(0, numrange):
    if (n <= 1):
        next = n
    else:
        next = value1 + value2 
        value1 = value2
        value2 = next
        
        print(next)
        
#reminder to self: make sure print is in the for statement or it WONT work