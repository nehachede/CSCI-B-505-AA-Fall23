#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:18:44 2023

@author: nehachede
"""

# use queue to store intermediate results

def generateCodes(n):
    if n<=0:
        return []
    
    queue = ['1'];
    temp = [];
    
    while n != 0:
        print(queue)
        print(temp)
        curr = queue.pop(0);
        # print(curr)
        a0 = curr + "0"
        a1 = curr + "1"

        temp.append(curr)
        
        queue.append(a0)
        queue.append(a1)
        n-=1
    return temp


print(generateCodes(5))
print(generateCodes(-2))
print(generateCodes(0))