#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:57:07 2018

@author: David
"""



#%%

#from functools import reduce

######## PRIVATE


######### PUBLIC

def string_calculator(string):
    if len(string) == 0:
        return 0
    
    numbers = string.split(",")
    total = 0
    for s in numbers:
        number = int(s)
        total = total + number
        
    return total

#def sumString(acc, s):
#    return acc + int(s)
#
#def string_calculator(string):
#    return 0 if len(string) == 0 else reduce(sumString, string.split(","), 0)
    

#########################################


def test_empty():
    assert string_calculator("") == 0
    
def test_single():
    assert string_calculator("4") == 4
    
def test_list():
    assert string_calculator("2,3,4,5") == 14