# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_s = set(a)
b_s = set(b)

ans = []
for i in range(n):
    if a[i] not in b_s:
        ans.append(a[i])

for i in range(m):
    if b[i] not in a_s:
        ans.append(b[i])

ans.sort()
print(*ans)
