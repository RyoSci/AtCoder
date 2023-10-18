# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
r = -1
cnt = 0
for l in range(n):
    while r+1 < n and cnt < k:
        cnt += a[r+1]
        r += 1

    if cnt >= k:
        ans += n-1-r+1

    cnt -= a[l]

print(ans)
