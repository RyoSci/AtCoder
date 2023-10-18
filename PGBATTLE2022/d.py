# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
MOD = 998244353
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)


d = [[0]*20 for _ in range(20)]
d[0][0] = 1

for i in range(20):
    for j in range(i+1):
        if 0 <= j-1:
            d[i][j] += d[i-1][j-1]

        if j < i:
            d[i][j] += d[i-1][j]


# print(d)


def nCk(n, k):
    return d[n][k]


ta1 = defaultdict(int)
at2 = defaultdict(int)


def f(i, key, val):
    if i == -1:
        return key, val
    for j in range(11):
        for k in range(2):
            if k == 0:
                tmp = (10-j)*a[i]
            else:
                tmp = (10-j)*a[i]+b[i]
            return val*f(i-1, tmp*key, val*d[10][j] % MOD) % MOD


f(1, 1, 1)

for i in range(n//2):
    tmp = defaultdict(int)
    for j in range(11):
        for k in range(2):
            if k == 0:
                key = (10-j)*a[i]
            else:
                key = (10-j)*a[i]+b[i]
            if key not in tmp:
                tmp[key] = 0
            tmp[key] += nCk(10, j)
            tmp[key] %= MOD

    res = defaultdict(int)
    for key, val in ta1.items():
        for kk, vv in tmp.items():
            res[key+kk] += val*vv
            res[key+kk] %= MOD
    ta1 = res

for i in range(n//2, n):
    tmp = defaultdict(int)
    for j in range(11):
        for k in range(2):
            if k == 0:
                key = (j-10)*a[i]
            else:
                key = (j-10)*a[i]+b[i]

            tmp[key] += nCk(10, j)
            tmp[key] %= MOD

    res = defaultdict(int)
    for key, val in at2.items():
        for kk, vv in tmp.items():
            res[key+kk] += val*vv
            res[key+kk] %= MOD
    at2 = res

ans = 0
for key, val in ta1.items():

    ans += val*at2[key]
    ans %= MOD

print(ans)

print(ta1)
print(at2)
