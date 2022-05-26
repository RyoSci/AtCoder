# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = max(a)
d = []
for i in range(n):
    if a[i] == c:
        d.append(i+1)

ans = "No"
for di in d:
    if di in b:
        ans = "Yes"

print(ans)
