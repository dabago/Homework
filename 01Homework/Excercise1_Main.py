#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 23:01:04 2018

@author: David
"""
#%%
import utils.Function
import data.Data_Triangles

def calculate_triangles():
    for i in data.Data_Triangles.triangle_definitions:
        print(utils.Function.area_triangle(i["base"],i["height"]))
    
calculate_triangles()

