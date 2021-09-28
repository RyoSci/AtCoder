from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = [-10**18, 10**18]+list(map(int, input().split()))
b.sort()

res = 10**18
for i in range(n):
    index = bisect_left(b, a[i])
    tmp = min(b[index]-a[i], a[i]-b[index-1])
    res = min(res, tmp)

print(res)
