# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, w = map(int, input().split())
a = list(map(int, input().split()))
ans = set()
for i in range(n):
    if a[i] <= w:
        ans.add(a[i])
    for j in range(i+1, n):
        if a[i]+a[j] <= w:
            ans.add(a[i]+a[j])
        for k in range(j+1, n):
            if a[i]+a[j]+a[k] <= w:
                ans.add(a[i]+a[j]+a[k])
print(len(ans))
