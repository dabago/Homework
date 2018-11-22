#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:37:21 2018

@author: David
"""


#%%

from eshop import checkout

def text_empty_list():
    values = []
    assert checkout([values]) == "You have nothing in your car"