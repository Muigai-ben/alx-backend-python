#!/usr/bin/env python3
''' a python module that returns the addition'''

def add(a: float, b: float) -> float:
     '''Float: The sum of a and b.'''
    return a + b

if __name__ == '__main__':  
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
