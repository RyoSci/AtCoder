# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

d = dict()
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 0
    d[a[i]] += 1

m = max(a)
ans = 0
for key, val in d.items():
    cnt = 1
    while key*cnt <= m:
        if cnt in d and key*cnt in d:
            ans += val*d[cnt]*d[key*cnt]
        cnt += 1

print(ans)
