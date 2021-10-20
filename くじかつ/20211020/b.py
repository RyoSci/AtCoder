import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, t = map(int, input().split())
n_ = n
flag = True
pre = 0
for i in range(m):
    a, b = map(int, input().split())
    if n-(a-pre) > 0:
        n -= a-pre
        n += b-a
        n = min(n, n_)
        pre = b
    else:
        flag = False
n -= t-pre

if n > 0 and flag:
    print("Yes")
else:
    print("No")
