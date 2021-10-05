#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:48:06 2021

@author: m18024598
"""
from matplotlib import pyplot

#def random_number(k):
#    number = random.random()
#    return number
    
#print(random_number(5))


random_numbers = []

def random_values(k):
    for i in range(k):
        random_numbers.append(random.random())
    return(random_numbers)
    
print(random_values(10))



x1 = random_values(10)
#y1 = 
fig,axes = pyplot.subplots(
    nrows = 1, ncols = 3,sharex=False, sharey=False
    )
axes[0]