import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0
for i in range(n):
    if v[i] > c[i]:
        ans += v[i]-c[i]

print(ans)
