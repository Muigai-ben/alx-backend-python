#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """
    Add two floats and return their sum.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == '__main__':
    print(add(3.5, 2.7))  
    print(add.__annotations__)
