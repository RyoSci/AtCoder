from bisect import bisect_left
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_s = sorted(x)

for i in range(n):
    index = bisect_left(x_s, x[i])
    if index < n//2:
        print(x_s[n//2])
    else:
        print(x_s[n//2-1])
