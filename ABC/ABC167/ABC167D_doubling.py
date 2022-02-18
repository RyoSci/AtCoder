import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

next = [[-1]*n for _ in range(100)]
g = [[] for i in range(n)]
for i in range(n):
    next[0][i] = a[i]-1

for i in range(100-1):
    for j in range(n):
        next[i+1][j] = next[i][next[i][j]]

now = 0
for i in range(100):
    if k >> i & 1:
        now = next[i][now]

print(now+1)
