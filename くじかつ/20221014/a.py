# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, x = map(int, input().split())
a = list(map(int, input().split()))
ans = INF

cnt = 0
for i in range(m):
    if x < a[i]:
        cnt += 1
ans = min(ans, cnt)

cnt = 0
for i in range(m):
    if x > a[i]:
        cnt += 1
ans = min(ans, cnt)
print(ans)
