"""
This module provides basic arithmetic functions for addition, subtraction,
multiplication, and division.
"""

def add(num_1, num_2):
    """Return the sum of two numbers."""
    return num_1 + num_2

def subtract(num_1, num_2):
    """Return the difference between two numbers."""
    return num_1 - num_2

def multiply(num_1, num_2):
    """Return the product of two numbers."""
    return num_1 * num_2

def divide(num_1, num_2):
    """
    Return the division of two numbers.
    Raises ValueError if b is 0.
    """
    if num_2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num_1 / num_2
