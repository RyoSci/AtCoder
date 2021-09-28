import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, a, b = map(int, input().split())

if n == 1:
    if a == b:
        ans = 1
    else:
        ans = 0
else:
    if a <= b:
        l = a*(n-1)+b
        r = b*(n-1)+a
        ans = r-l+1
    else:
        ans = 0

print(ans)
