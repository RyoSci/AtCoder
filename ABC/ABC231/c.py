from bisect import bisect_left
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(q):
    x = int(input())
    ans = n-bisect_left(a, x)
    print(ans)
