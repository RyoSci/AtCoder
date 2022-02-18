from bisect import bisect_right
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

a = []

for i in range(n):
    a.append(sum(p[i]))


a.sort()
for i in range(n):
    p_s = sum(p[i])+300
    index = bisect_right(a, p_s)
    if n-index+1 <= k:
        print("Yes")
    else:
        print("No")
