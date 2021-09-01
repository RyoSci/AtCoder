import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
d = [0]*k

for i in range(1, n+1):
    d[i % k] += 1

res = 0
for a in range(0, k):
    if 2*a % k == 0:
        res += d[a]*d[a]*d[-a % k]

print(res)
