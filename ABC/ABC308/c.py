# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import gcd
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


# Fractionは下記を引用
# https: // github.com/toriitakuto/Library_for_python/blob/main/Fraction.py


class Fraction:
    def __init__(self, num, den=1):

        self.num = num
        self.den = den

    def __gt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 * den2 > num2 * den1


tot = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    tot.append([Fraction(a, a+b), -i])

tot.sort(reverse=True)

ans = []
for i in range(n):
    ans.append(-tot[i][1]+1)

print(*ans)
