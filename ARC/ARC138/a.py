# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, k = map(int, input().split())
a = list(map(int, input().split()))
m = n-k

b = [[a[i], i] for i in range(k, n)]
b.sort()

num = []
pos = []

for i in range(m):
    num.append(b[i][0])
    pos.append(b[i][1])

for i in range(m-1, 0, -1):
    pos[i-1] = min(pos[i-1], pos[i])

num.append(INF)

ans = INF
for i in range(k):
    now = bisect_right(num, a[i])
    if num[now] == INF:
        continue
    ans = min(ans, pos[now]-i)

if ans == INF:
    print(-1)
else:
    print(ans)
