#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:19:46 2019

@author: john
"""

class Person:
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25


class ModifiedPerson(Person):
    def __init__(self):
        super().__init__()
    
    def __repr__(self):
        return f"<ModifiedPerson Class - fname: {self.fname}, lname: {self.lname}, age: {self.age}"
    
    def __str__(self):
        return f'ModifiedPerson ({self.fname} {self.lname} is {self.age})'

    def __bytes__(self):
        val = f'ModifiedPerson:{self.fname}:{self.lname}:{self.age}'
        return bytes(val.encode('utf-8'))

def main():
    cls1 = Person()
    
    print(repr(cls1))
    print(str(cls1))
    print(f'Formatted: {cls1}')
    # print(bytes(cls1))  # Cannot convert to bytes
    
    cls2 = ModifiedPerson()
    print(repr(cls2))
    print(str(cls2))
    print(f'Formatted: {cls2}')
    print(bytes(cls2))


if __name__ == "__main__":
    main()
