import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
l = max(a, c)
r = min(b, d)

if r-l+1 > 0:
    print("Yes")
else:
    print("No")
