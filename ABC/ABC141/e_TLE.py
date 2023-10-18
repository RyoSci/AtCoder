# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
from collections import defaultdict
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18
"https://tjkendev.github.io/procon-library/python/string/rolling_hash.html"
"https://kyoroid.github.io/algorithm/string/rolling_hash.html"

# 1-dimension Rolling Hash


class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        """S[l, r) のハッシュを求める"""
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

    def connect(self, h1, h2, h2len):
        """S1+S2 のハッシュを、それぞれのハッシュから求める"""
        return (h1*self.pw[h2len] + h2) % self.mod

    def lcp(self, l1, r1, l2, r2):
        """S[l1, r1) とS[l2, r2) の最大共通接頭辞を求める"""
        # LCPの最小値 (範囲内)
        low = 0
        # LCPの最大値 + 1 (範囲外)
        high = min(r1-l1, r2-l2) + 1
        while high - low > 1:
            mid = (high + low) // 2
            if self.get(l1, l1 + mid) == self.get(l2, l2 + mid):
                low = mid
            else:
                high = mid
        return low


base = 37
mod0 = 1000000007
mod1 = 100000000000031

# 衝突が怖いなら数回判定する
"https://snuke.hatenablog.com/entry/2017/02/03/035524"

n = int(input())
s = input()

rh0 = RollingHash(s, base, mod0)
# rh1 = RollingHash(s, base, mod1)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        ans = max(ans, rh0.lcp(i, j, j, n))
print(ans)
