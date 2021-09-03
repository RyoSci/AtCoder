import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

res = 0
now = a[0]
for i in range(n):
    if now > a[i]:
        res += now-a[i]
    else:
        now = a[i]

print(res)
