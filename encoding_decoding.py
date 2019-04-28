#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:01:42 2019

@author: john
"""
from binascii import hexlify

a = 'hello there, how are you?'
bytes_a = a.encode()
hex_a = hexlify(bytes_a).decode()

print('string,bytes_string,hexidecimal_string')
print(f'"{a}","{bytes_a}","{hex_a}"')
