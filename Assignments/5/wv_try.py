#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:50:01 2023

@author: nehachede
"""

class Node:
    def __init__(self, data, left=None, right=None, bmap=None):
        self.data = data
        self.left = left
        self.right = right
        self.bmap = bmap

class Wavelet_Tree:
    def __init__(self, A: list[int] = []):
        self.root = None
        self.build_tree_and_bitmaps(A)

    def build_tree_and_bitmaps(self, A, node=None):
        if not A:
            return None

        mid = len(A) // 2
        node = Node(mid)

        l = r = []
        bmap = [0] * len(A)

        for i in range(len(A)):
            if A[i] <= node.data:
                l.append(A[i])
                bmap[i] = 1
            else:
                r.append(A[i])

        node.bmap = bmap
        node.left = self.build_tree_and_bitmaps(l, node.left)
        node.right = self.build_tree_and_bitmaps(r, node.right)
        
        if self.root is None:
            self.root = node

        return node

    def get_wavelet_level_order(self):
        q = [self.root]
        lvl = []

        while q:
            node = q.pop(0)
            lvl.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return lvl

    def rank(self, character, position):
        pos = 0

        while self.root.left or self.root.right:
            if character <= self.root.data:
                self.root = self.root.left
            else:
                pos += self.root.bmap[position]
                self.root = self.root.right
        return pos + position

# Example usage:
A = [6, 2, 0, 7, 7, 9, 3, 1, 8, 5, 4]
T = Wavelet_Tree(A)
print(T.get_wavelet_level_order())
print(T.rank(7, 5))
