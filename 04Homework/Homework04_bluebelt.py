#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:36:32 2018

@author: David
"""
#%%

g = {
        "a": ["b", "c", "d"],
        "b": ["c", "a", "d"],
        "c": ["a", "b", "d"],
        "d": ["a", "b", "c"]
        }

#print(len(g))

def fully_connected(g):
    print (len(g))
    for key in g:
        print(len(g[key]))
        if len(g) - 1 == len(g[key]):
            print(key)
    return "okokok"
       


        

fully_connected(g)



