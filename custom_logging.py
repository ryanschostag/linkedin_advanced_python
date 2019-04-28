#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:19:58 2019

@author: john
"""

import logging


extra_data = {
    'user': 'joem@example.com'
}


def anotherFunction():
    logging.debug("This is a debug level log", extra=extra_data)


def main():
    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(
        filename="output.log",
        level=logging.DEBUG,
        filemode='w',
        format=fmtstr,
        datefmt=datestr
    )
    
    logging.info("This is an info-level log message", extra=extra_data)
    logging.warning("This is a warning-level message", extra=extra_data)
    anotherFunction()

if __name__ == "__main__":
    main()
