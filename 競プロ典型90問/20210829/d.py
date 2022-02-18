import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = [0]*(n+1)

for i in range(2, n+1):
    if a[i] != 0:
        continue
    for j in range(i, n+1, i):
        a[j] += 1

res = 0
for i in range(n+1):
    if a[i] >= k:
        res += 1

print(res)
