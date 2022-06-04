# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
d = [dict() for _ in range(k)]

for i in range(n):
    if a[i] not in d[i % k]:
        d[i % k][a[i]] = 0
    d[i % k][a[i]] += 1

a.sort()
ans = "Yes"
for i in range(n):
    if a[i] in d[i % k] and d[i % k][a[i]] > 0:
        d[i % k][a[i]] -= 1
    else:
        ans = "No"
        break

print(ans)
