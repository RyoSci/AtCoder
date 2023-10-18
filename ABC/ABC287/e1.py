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
mod0 = 1000000007
mod1 = 100000000000031

# 衝突が怖いなら数回判定する


n = int(input())
d0 = dict()
d1 = dict()

s0 = []
s1 = []
for i in range(n):
    si = input()
    m = len(si)
    rh0 = RollingHash(si, base, mod0)
    rh1 = RollingHash(si, base, mod1)

    hashes0 = []
    hashes1 = []
    for j in range(m+1):

        tmp = rh0.get(0, j)
        if tmp not in d0:
            d0[tmp] = 0
        d0[tmp] += 1
        hashes0.append(tmp)

        tmp = rh1.get(0, j)
        if tmp not in d1:
            d1[tmp] = 0
        d1[tmp] += 1
        hashes1.append(tmp)

    s0.append(hashes0)
    s1.append(hashes1)


for i in range(n):
    ans = 0
    for j, (h0, h1) in enumerate(zip(s0[i], s1[i])):
        if d0[h0] > 1 and d1[h1] > 1:
            ans = j

    print(ans)
