from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n-1):
    a[i+1] += a[i]
for i in range(m-1):
    b[i+1] += b[i]

a = [0]+a
res = 0
for i in range(n+1):
    if a[i] > k:
        continue
    tmp = i
    tmp += bisect_right(b, k-a[i])
    res = max(res, tmp)

print(res)
