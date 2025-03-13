#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:16:52 2023

@author: nehachede
"""

def findsum(root, targetSum):
    current = root
    
    def traverse(node, csum):
        
        if node is None:
            return False
        
        # leaf node
        if node.left is None and node.right is None and csum+node.val == targetSum:
            return True

        return traverse(node.left, csum + node.val) or traverse(node.right, csum+node.val)
    
    csum = 0
    if traverse(current, csum):
        return True
    return False

# def findsum(root, targetSum):

#     def sum(node):
#         if node is None:
#             return 0
    
#         return (sum(node.left) + sum(node.right) + node.val)
    
#     if sum(root) == targetSum:
#         return True
    
#     return False