# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 17:36:37 2022

@author: venus
"""
print ("task one")

pi=3.14

print ("note: the value of pi is", pi)
radius = input("Please enter the radius of a circle: ") 
radius = float(radius)

area = radius * 3.14 * radius
print ("the area of the circle is", area)

print ("task two")

filename = input("Please enter the filename of the program:")

fileextenstion = filename.split(".")

print ("the extension of the file is " + fileextenstion[-1])