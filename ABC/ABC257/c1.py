# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
w = list(map(int, input().split()))
ws = []

for i in range(n):
    ws.append((w[i], int(s[i])))

ws.sort()
w.sort()

chs = [0]*(n+1)
for i in range(n):
    if ws[i][1] == 0:
        chs[i+1] = 1

for i in range(n):
    chs[i+1] += chs[i]

totad = 0
for i in range(n):
    if s[i] == "1":
        totad += 1


ans = 0
for i in range(n):
    wi, si = ws[i]

    for j in (1, -1):
        chi = bisect_right(w, wi+0.5*j)
        chnum = chs[chi]
        adnum = chi-chnum
        ans = max(ans, chnum+totad-adnum)


print(ans)
