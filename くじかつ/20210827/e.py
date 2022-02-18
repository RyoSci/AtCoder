import sys
from bisect import bisect_left

input = sys.stdin.readline

a, b, q = map(int, input().split())

s = [int(input()) for _ in range(a)]+[-10**18, 10**18]
t = [int(input()) for _ in range(b)]+[-10**18, 10**18]
s.sort()
t.sort()

for i in range(q):
    x = int(input())
    sr = bisect_left(s, x)
    tr = bisect_left(t, x)
    res1 = max(abs(s[sr-1]-x), abs(t[tr-1]-x))
    res2 = abs(s[sr-1]-x)+abs(t[tr]-x)+min(abs(s[sr-1]-x), abs(t[tr]-x))
    res3 = abs(s[sr]-x)+abs(t[tr-1]-x)+min(abs(s[sr]-x), abs(t[tr-1]-x))
    res4 = max(abs(s[sr]-x), abs(t[tr]-x))
    print(min(res1, res2, res3, res4))
