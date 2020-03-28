"""
Title: Taylor Series Approximations
Author: Dominic Vicharelli
Description: creates Taylor Series approximations for sin(), cos(), and e^().
"""
import math


def sine_approx(n: int, x: float) -> float:
    """
    computes and returns T_n(x) where T_n() is the nth degree Taylor
    polynomial for sine.
    """
    value = 0
    for i in range(0, (int(n)//2 + 1)):
        value += (((-1)**i) / (math.factorial(2*i + 1))) * (x**(2 * i + 1))
    return value


def cosine_approx(n: int, x: float) -> float:
    """
    computes and returns T_n(x) where T_n() is the nth degree Taylor
    polynomial for cosine.
    """
    value = 0
    for i in range(0, (int(n)//2 + 1)):
        value += (((-1)**i) / (math.factorial(2*i))) * (x**(2*i))
    return value


def exp_approx(n: int, x: float) -> float:
    """
    computes and returns T_n(x) where T_n() is the nth degree Taylor
    polynomial for the exponential function.
    """
    value = 0
    for i in range(0, n+1):
        value += (x**i) / (math.factorial(i))
    return value

