#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:54:52 2019

@author: john
"""

def main():
    # define two lists of numbers
    evens = list(range(0, 20, 2))
    odds = list(range(1, 21, 2))
    
    even_squared = list(
        map(
                lambda e: e**2, 
                filter(lambda e: e > 4 and e < 16, evens)
        )
    )
    print(even_squared)
    
    even_squared = [e**2 for e in evens if e > 4 and e < 16]
    print(even_squared)
    
    odd_squared = [e**2 for e in odds if e > 3 and e < 17]
    print(odd_squared)

if __name__ == "__main__":
    main()
