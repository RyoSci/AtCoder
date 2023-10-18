# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


"https://tjkendev.github.io/procon-library/python/string/rolling_hash.html"

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
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

    def connect(self, h1, h2, h2len):
        return (h1*self.pw[h2len] + h2) % self.mod


base = 37
mod = 1000000087

n = int(input())
s = input()
rs = s[::-1]

rh = RollingHash(s, base, mod)
rrh = RollingHash(rs, base, mod)


for i in range(n+1):
    head = rh.get(0, i)
    tail = rh.get(2*n-(n-i), 2*n)
    nor = rh.connect(head, tail, n-i)
    rev = rrh.get(2*n-i-n, 2*n-i)

    # print(i, s[:i]+s[2*n-(n-i):], rs[2*n-i-n:2*n-i])
    if nor == rev:
        print(s[:i]+s[2*n-(n-i):])
        print(i)
        exit()

print(-1)
