# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

m = int(input())
g = [[] for _ in range(9)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    g[u].append(v)
    g[v].append(u)

p = list(map(int, input().split()))
invp = [-1]*9
for i in range(8):
    invp[p[i]-1] = i

for i in range(9):
    if invp[i] == -1:
        b = i

dp = dict()

q = deque()
q.append([invp, b, 0])
dp[tuple(invp)] = 0

while len(q):
    invp, b, d = q.popleft()

    for nb in g[b]:
        invp[b], invp[nb] = invp[nb], invp[b]
        nxtp = tuple(invp)
        if nxtp not in dp:
            dp[nxtp] = d+1
            q.append([invp[::], nb, d+1])
        invp[b], invp[nb] = invp[nb], invp[b]

p2 = list(range(1, 9))
invp = [-1]*9

for i in range(8):
    invp[p2[i]-1] = i
invp = tuple(invp)

if invp not in dp:
    print(-1)
else:
    print(dp[invp])
