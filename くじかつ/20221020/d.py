# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = [0]+list(map(int, input().split()))

b = [0]*(n+1)
for i in range(n, 0, -1):
    tot = 0
    for j in range(i*2, n+1, i):
        tot += b[j]

    if tot % 2 != a[i]:
        b[i] = 1

ans = []
for i in range(1, n+1):
    if b[i] == 1:
        ans.append(i)

print(len(ans))
if len(ans) > 0:
    print(*ans)
