import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
d = dict()

for i in range(n):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = 0
    if a+b not in d:
        d[a+b] = 0
    d[a] += 1
    d[a+b] -= 1

res = [0]*(n+1)

d_keys = sorted(list(d.keys()))

now = 0
m = len(d)

for i in range(m-1):
    key = d_keys[i]
    next_key = d_keys[i+1]
    now += d[key]
    res[now] += next_key-key

print(*res[1:])
