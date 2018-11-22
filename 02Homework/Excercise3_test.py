#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:10:40 2018

@author: David
"""

from Excercise3 import create_product,checkout

guitar = create_product ("Guitar",1000)
pick_box = create_product ("Pick box", 5)
guitar_strings = create_product ("Guitar strings",10)
insurance = create_product ("Insurance",5)
priority_mail = create_product ("Priority mail",10)


def test_checkout_with_normal_tier():
    cart= [guitar, insurance,priority_mail]
    tier = "Normal"
    assert checkout(cart,tier) == 1015
    

def test_checkout_with_silver_tier():
    cart= [guitar,guitar, insurance,priority_mail]
    tier = "Silver"
    assert checkout(cart,tier) == 1855
    
def test_checkout_with_gold_tier():
    cart= [guitar,guitar, insurance,priority_mail,insurance,pick_box,guitar_strings]
    tier = "Gold"
    assert checkout(cart,tier) == 1928.5
    
    
def test_empty3():
    cart = []
    tier = "Gold"
    assert checkout (cart,tier) == None
    

    
    