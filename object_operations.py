#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:11:53 2019

@author: john
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    

def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    
    p3 = p1 + p2
    print(p3)
    
    p4 = p2 - p1
    print(p4)
    
    p1 += p2
    print(p1)


if __name__ == "__main__":
    main()
    