#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:32:05 2023

@author: nehachede
"""
import matplotlib.pyplot as plt

def bp(num_people):
    p_not = 1.0
    for i in range(num_people):
        p_not *= (365 - i) / 365

    return 1 - p_not

n = list(range(1, 100))
p = [bp(i) for i in n]

plt.plot(n, p)
plt.title('Birthday Paradox')
plt.xlabel('N')
plt.ylabel('Probability')
plt.show()
