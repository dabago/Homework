#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:25:40 2018

@author: David
"""

#%%



#%%

######## PRIVATE

def convert_to_numbers(string):
    if len(string) == 0:
        return []
    strings = string.split(",")
    numbers = []
    for s in strings:
        number = int(s)
        numbers = numbers + [number]
    return numbers

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

convert_to_numbers("")

######### PUBLIC

def string_calculator(string):
    numbers = convert_to_numbers(string)
    total = sum_numbers(numbers)
    return total
    

#########################################


#def test_empty():
#    assert string_calculator("") == 0
#    
#def test_single():
#    assert string_calculator("4") == 4
#    
#def test_list():
#    assert string_calculator("2,3,4,5") == 14