# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

divs = []
for i in range(1, n+1):
    if i*i > n:
        break
    if n % i != 0:
        continue

    divs.append(i)
    if i != n//i:
        divs.append(n//i)

divs.remove(n)
divs.sort()

m = len(divs)
b = dict()

mod = 998244353
for i in divs:
    cnt = 1
    for j in range(i):
        go = False
        for k in range(j, n, i):
            if s[k] == ".":
                go = True
                break
        if not go:
            cnt *= 2
            cnt %= mod

    b[i] = cnt


a = dict()
ans = 0
for div in divs:
    tmp_divs = []

    for j in range(1, div+1):
        if j*j > div:
            break

        if div % j > 0:
            continue

        tmp_divs.append(j)
        if j != div//j:
            tmp_divs.append(div//j)

    tmp_divs.remove(div)

    a[div] = b[div]
    for j in tmp_divs:
        a[div] -= a[j]
        a[div] %= mod

    ans += a[div]
    ans %= mod

print(ans)
