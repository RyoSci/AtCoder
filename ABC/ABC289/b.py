# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
p = list(map(int, input().split()))

q = [0] * (n+1)
for i in p:
    q[i] = 1

ans = []


def dfs(i):
    seen[i] = 1
    if i == n+1:
        return

    if q[i]:
        dfs(i+1)

    ans.append(i)


seen = [0]*(n+1)
for i in range(n):
    if seen[i+1]:
        continue
    dfs(i+1)

print(*ans)
