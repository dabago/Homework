#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:52:00 2018

@author: David
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:59:21 2018

@author: David
"""

#%%

graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": ["e"],
        "e": ["empty"]
        }
 

def get_all_nodes(g):
    nodes = []
    
    for node in g:
        nodes.append(node)
    
    return nodes


get_all_nodes(graph)



def get_all_edges(g):
    edges = []
    
    for node in g:
        print("this node is " + node)
        for other_node in g[node]:
            print("This " + node + " connects with " + other_node)
            edges.append(node + " -> " + other_node)

    return edges


get_all_edges(graph)

#%%
graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["d"],
        "d": ["e"],
        "e": [],
        "f": [],
        "g": [],
        "h": []
        
        }



def non_connected(g):
    node_not_connected = []
    lst_g_values = []
  
    
    for key in g:
        print(key)
        lst_g_values.append(g[key])

        print (lst_g_values)
        if g[key] == [] and [key] not in lst_g_values:
            print(g[key])
            node_not_connected.append(key)
           
    return "The node that is/are not connected is/are " + str(node_not_connected)

non_connected(graph)




