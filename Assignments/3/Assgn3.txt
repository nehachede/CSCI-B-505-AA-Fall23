#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:45:25 2023

@author: nehachede
"""

def who_wins(n, k):
    if n == 1:
        return 1
    
    return (who_wins(n - 1, k) + k - 1) % n + 1

def count_successful_school_commutes(home_coords, school_coords, N):
    def path(home_coord, school_coord):
        x1, y1 = home_coord
        x2, y2 = school_coord

        if x1 == x2 and y1 == y2:
            return True
        if (x1 + y1) <= x2 and y1 <= y2 and path((x1 + y1, y1), school_coord):
            return True
        if x1 <= x2 and (x1 + y1) <= y2 and path((x1, x1 + y1), school_coord):
            return True
        return False

    result = 0
    for i in range(N):
        if path(home_coords[i], school_coords[i]):
            result += 1
    return result

def zenthar_puzzle(n, k):
    if n <= 0:
        return []

    result = queue = []
    queue = [str(i) for i in range(1, 10)]

    while queue:
        curr = queue.pop(0)

        if len(curr) == n:
            result.append(int(curr))
        else:
            left = int(curr[-1])

            for diff in (-k, k):
                right = left + diff

                if right in range(0,10):
                    queue.append(curr + str(right))
    return result

def decompress(s):
    
    if(not(s and s.strip())):
        return ""
    
    stack = []
    num = 0
    decompressed_string = ""
    
    for char in s:
        if char.isdigit():
            num = int(char)
        elif char == '(':
            stack.append((num, decompressed_string))
            num = 0
            decompressed_string = ""
        elif char == ')':
            count, partial_str = stack.pop()
            decompressed_string = partial_str + decompressed_string * count
        else:
            decompressed_string += char
    return decompressed_string

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def create_bt_count_oracles_extract(values, k) -> bool:
    if not values:
        return False

    root = TreeNode(values[0])
    queue = [(root, values[0], 1)]
    count = 1

    while queue:
        node, val_max, idx = queue.pop(0)
        
        idx_l = 2 * idx
        idx_r = 2 * idx + 1
        
        if idx_l <= len(values):
            val_l = values[idx_l - 1]
            if val_l >= val_max:
                count += 1
            left = TreeNode(val_l)
            node.left = left
            queue.append((left, max(val_max, val_l), idx_l))

        if idx_r <= len(values):
            val_r = values[idx_r - 1]
            if val_r >= val_max:
                count += 1
            right = TreeNode(val_r)
            node.right = right
            queue.append((right, max(val_max, val_r), idx_r))

        if count >= k:
            return True

    return False

def solve_puzzle(root):
    if not root:
        return []
    
    queue = [root]
    levels = []
    
    while queue:
        next_queue = []
        level = []
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        levels.append(level)
        queue = next_queue
    
    result = []
    
    for i in range(len(levels)):
        prod = 1
        for j in range(len(levels[i])):
            prod *= levels[i][j]
        result.append(prod)

    return result.index(max(result)) + 1

def TreeOfNumbers(root) -> int:
    if root is None:
        return 0
    
    def dfs(node, res):
        if not node:
            return 0
        
        res = res * 10 + node.data
        
        if not node.left and not node.right:
            return res
        
        return dfs(node.left, res) + dfs(node.right, res)
    
    return dfs(root, 0)

class amor_dict():
    def __init__(self, num_list=None):
        self.levels = {}

        if num_list is not None:
            for num in num_list:
                self.insert(num)
                
    def merge(self, ai, h):
        merged = []
        i, j = 0, 0

        while i < len(ai) and j < len(h):
            if ai[i] < h[j]:
                merged.append(ai[i])
                i += 1
            else:
                merged.append(h[j])
                j += 1

        merged.extend(ai[i:])
        merged.extend(h[j:])
        return merged
    
    def insert(self, element):
        i = 0
        H = [element]

        while i in self.levels:
            H = self.merge(self.levels[i], H)
            del self.levels[i]
            i += 1

        self.levels[i] = H

    def print(self):
        max_level = max(self.levels.keys()) if self.levels else 0
        result = []

        for i in range(max_level + 1):
            result.append(self.levels.get(i, []))

        return result
    
    def search(self, num):
        for level, num_list in self.levels.items():
            left, right = 0, len(num_list) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if num_list[mid] == num:
                    return level
                elif num_list[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 