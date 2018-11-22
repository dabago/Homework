#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 02:05:41 2018

@author: David
"""

#%%

from Excercise1 import checkout, create_product

guitar = create_product ("Guitar",1000)
pick_box = create_product ("Pick box", 5)
guitar_strings = create_product ("Guitar strings",10)
insurance = create_product ("Insurance",5)
priority_mail = create_product ("Priority mail",10)


def test_checkout_g_i_p():
    cart= [guitar, insurance,priority_mail]
    assert checkout(cart) == 1015
    

def test_checkout_g_g_i_p():
    cart= [guitar,guitar, insurance,priority_mail]
    assert checkout(cart) == 2015
    
def test_checkout_g_g_i_p_i_p_g():
    cart= [guitar,guitar, insurance,priority_mail,insurance,pick_box,guitar_strings]
    assert checkout(cart) == 2035