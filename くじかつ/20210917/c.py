from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())))

res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        rest = l[-i-1]-l[-j-1]+1
        idx = bisect_left(l, rest)
        res += max(0, n-j-1-idx)

print(res)
