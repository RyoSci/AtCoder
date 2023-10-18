# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k, q = list(map(int, input().split()))
a = list(map(lambda x: int(x)-1, input().split()))
l = list(map(lambda x: int(x), input().split()))

b = [0]*n

for i in range(k):
    b[a[i]] = i+1

for i in range(q):
    cnt = 0
    for j in range(n):
        if b[j] > 0:
            cnt += 1
        if j != n-1 and cnt == l[i] and b[j+1] == 0:
            b[j+1] = b[j]
            b[j] = 0

ans = [0]*k
for i in range(n):
    if b[i] > 0:
        ans[b[i]-1] = i+1

print(*ans)
