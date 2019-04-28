#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:42:44 2019

@author: john
"""

import logging


def main():
#    logging.basicConfig(
#        level=logging.DEBUG,
#        filename='basic_logging.log'
#    )
    logging.basicConfig(
        filename='basic_logging.log',
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',
        filemode='w'
    )
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")
    
    logging.info(f"Here's a {'string'} variable and an int: {10}")


if __name__ == "__main__":
    main()
