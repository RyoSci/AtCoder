# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
s = []
for i in range(h):
    si = input()
    s.append(si)


q = deque()
seen = [[0]*(w) for _ in range(h)]
if s[0][0] == "s":
    q.append((0, 0, 0))
    seen[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
snuke = "snuke"
while len(q):
    cnt, i, j = q.popleft()

    for ii in range(4):
        ni = i+dx[ii]
        nj = j+dy[ii]

        if 0 <= ni < h and 0 <= nj < w and snuke[(cnt+1) % 5] == s[ni][nj] and seen[ni][nj] == 0:
            q.append((cnt+1, ni, nj))
            seen[ni][nj] = 1

if seen[h-1][w-1]:
    print("Yes")
else:
    print("No")
