import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

b = [0, 360]

now = 0
for i in range(n):
    now += a[i]
    now %= 360
    b.append(now)

b.sort()
ans = 0
for i in range(n+1):
    ans = max(ans, b[i+1]-b[i])

print(ans)
