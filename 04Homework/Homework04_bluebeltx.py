#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:36:32 2018

@author: David
"""
#%%
import networkx as nx
import matplotlib.pyplot as plt 

g = {
        "a": ["b", "c"],
        "b": ["c", "a"],
        "c": ["a", "b"],
        
        }

#print(len(g))

def fully_connected(g):
    master_lst = []
    for node in g:
        print ("This node is " + node)
        master_lst.append(node)
#        print(master_lst)
    
        for i in master_lst:
             print (i)
             if i == node and i not in g[node]:
                 pass
                
            for i in master_lst:
                print ( i)
        
            return True
         
            
                
            
    
#    for value in g[node]:
#        print(value)
#        if node in master_lst :
#            if value in master_lst:
#                    print ("This is the value " + value)
#                    print (g[node])
##                return True
#           
#    print("The master list is " + str(master_lst))
       




fully_connected(g)



