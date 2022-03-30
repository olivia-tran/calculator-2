"""Functions for common math operations."""


def is_valid():
    """checks if inputs are float
    """
    pass


def add(num1, num2):
    """Return the sum of num1 and num2."""

    return num1 + num2


def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    return num1 * num2


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "The denominator cannot be zero. "


def square(num1):
    """Return the square of num1."""
    return num1 ** num1


def cube(num1):
    """Return the cube of num1."""
    return num1 ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1 ** num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    try:
        return num1 % num2
    except ZeroDivisionError:
        return "The denominator cannot be zero. "
