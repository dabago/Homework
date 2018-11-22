#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 01:36:47 2018

@author: David
"""

#%%
from Excercise1 import checkout, create_product

guitar = create_product ("Guitar",1000)
pick_box = create_product ("Pick box", 5)
guitar_strings = create_product ("Guitar strings",10)
insurance = create_product ("Insurance",5)
priority_mail = create_product ("Priority mail",10)



def test_empty():
    inventory = []
    assert checkout (inventory) == None

def test_all ():
    inventory = [
    guitar,pick_box,guitar_strings
            ]
    
    assert checkout(inventory) == 1015
    

def test_2x_guitar ():
    inventory = [
    guitar,guitar
        ]
    assert checkout(inventory) == 2000
        

def test_2x_guitar_guitar_strings():
    inventory = [
    guitar,guitar,guitar_strings
        ]
        
    assert checkout(inventory) == 2010
    