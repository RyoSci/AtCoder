# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


tot = []
q = deque()
for i in range(10):
    tot.append(i)
    q.append(i)

while len(q):
    now = q.popleft()
    last = now % 10

    for i in range(last):
        nx = now*10+i
        tot.append(nx)
        q.append(nx)

k = int(input())
tot.sort()
print(tot[k])
