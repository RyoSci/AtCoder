# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import gcd
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# Fractionは下記を引用
# https: // github.com/toriitakuto/Library_for_python/blob/main/Fraction.py


class Fraction:
    def __init__(self, num, den=1):
        if type(num) == float or type(num) == str:
            assert den == 1
            if type(num) == float:
                S = str("{:.10f}".format(num))
            else:
                S = num
            N = len(S)
            point = -1
            for i in range(N):
                if S[i] == ".":
                    point = i
            if point != -1:
                F = Fraction(int(S[:point] + S[point + 1:]),
                             10 ** (N - 1 - point))
            else:
                F = Fraction(int(S), 1)
            self.num = F.num
            self.den = F.den
        elif type(num) == type(den) == int:
            # assert den != 0
            # """
            inf = 10**9
            if den == 0:
                if num > 0:
                    self.num = inf
                    self.den = 1
                elif num < 0:
                    self.num = -inf
                    self.den = 1
                else:
                    raise Exception
                return
            # """
            den, num = max((den, num), (-den, -num))
            g = gcd(den, num)
            self.num = num // g
            self.den = den // g
        else:
            raise Exception

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __pos__(self):
        return self

    def __neg__(self):
        num, den = self.num, self.den
        return Fraction(-num, den)

    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return Fraction(num1 * den2 + num2 * den1, den1 * den2)

    def __sub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return Fraction(num1 * den2 - num2 * den1, den1 * den2)

    def __mul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return Fraction(num1 * num2, den1 * den2)

    def __truediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return Fraction(num1 * den2, num2 * den1)

    def __pow__(self, x):
        assert type(x) == int
        num, den = self.num, self.den
        if x >= 0:
            return Fraction(num**x, den**x)
        else:
            return Fraction(den ** (-x), num ** (-x))

    __radd__ = __add__

    def __rsub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = other.num, other.den
        num2, den2 = self.num, self.den
        return Fraction(num1 * den2 - num2 * den1, den1 * den2)

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = other.num, other.den
        num2, den2 = self.num, self.den
        return Fraction(num1 * den2, num2 * den1)

    def __eq__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 == num2 and den1 == den2

    def __lt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 * den2 < num2 * den1

    def __le__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 * den2 <= num2 * den1

    def __gt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 * den2 > num2 * den1

    def __ge__(self, other):
        if type(other) != Fraction:
            other = Fraction(other)
        num1, den1 = self.num, self.den
        num2, den2 = other.num, other.den
        return num1 * den2 >= num2 * den1

    def floor(self):
        return self.num//self.den


n = int(input())

d0 = defaultdict(int)
d1 = defaultdict(int)
zz = 0
az = 0
bz = 0
for i in range(n):
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        zz += 1
    # elif a == 0:
    #     d0[(0, 1)] += 1
    #     d1[(-1, 0)] += 1
    #     # az += 1
    # elif b == 0:
    #     d0[(1, 0)] += 1
    #     d1[(0, -1)] += 1
    #     # bz += 1

    else:
        tmp = Fraction(a, b)
        d0[(tmp.num, tmp.den)] += 1
        tmp = Fraction(-b, a)
        d1[(tmp.num, tmp.den)] += 1

mod = 10**9+7
ans = 1
# ans *= pow(2, az, mod)-1 + pow(2, bz, mod)-1 + 1
for key, val in d0.items():
    rval = d1[key]
    tmp = Fraction(-key[1], key[0])
    rkey = (tmp.num, tmp.den)
    d1[rkey] = -1

    if rval == -1:
        continue

    res = pow(2, val, mod)-1 + pow(2, rval, mod)-1 + 1

    ans *= res % mod
    ans %= mod

ans += zz
ans -= 1
print(ans % mod)
