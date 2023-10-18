# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, k = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()
for i in range(n):
    dq.append(a[i])

for i in range(k):
    dq.popleft()
    dq.append(0)

print(*dq)
