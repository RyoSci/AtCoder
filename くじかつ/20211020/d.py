import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
t = 0

res = 1
for i in range(n-1):
    t += a[i]
    if 2*t >= a[i+1]:
        res += 1
    else:
        res = 1

print(res)
