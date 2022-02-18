import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

res = 0
for i in range(n-1):
    if a[i]+a[i+1] <= x:
        continue
    else:
        dis = a[i]+a[i+1]-x
        res += dis
        tmp = min(a[i+1], dis)
        a[i+1] -= tmp
        a[i] -= dis-tmp
print(res)
