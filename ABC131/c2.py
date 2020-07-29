import math
from typing import List

a, b, c, d = map(int, input().split())

def gcd(c, d):
    mod = 1
    while mod > 0:
        mod = c % d
        c = d
        d = mod
    return c

def f(x: int, c: int, d: int):
    return x - x // c - x // d + x // (c * d // gcd(c, d))

print(f(b, c, d) - f(a - 1, c, d))
