# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

# n = 2*10**5
# a = [1]*n

m = 10**6+10
d = [0]*m
for i in range(n):
    d[a[i]] += 1

for i in range(1, m):
    if d[i] == 0:
        continue
    for j in range(i, m, i):
        d[j] += 1

ans = 0
for i in range(n):
    if d[a[i]] == 2:
        ans += 1

print(ans)
