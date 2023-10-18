# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n = int(input())
a = list(map(int, input().split()))
a.sort()
rest = 0
d = deque()
d.append(a[0])
for i in range(1, n):
    if a[i-1] == a[i]:
        rest += 1
    else:
        d.append(a[i])

cnt = 1
for i in range(1, n+1):
    if len(d) > 0 and d[0] == cnt:
        cnt += 1
        d.popleft()
    else:
        if rest >= 2:
            rest -= 2
            cnt += 1
        elif rest == 1 and len(d) > 0:
            cnt += 1
            rest -= 1
            d.pop()
        elif len(d) >= 2:
            d.pop()
            d.pop()
            cnt += 1

print(cnt-1)
