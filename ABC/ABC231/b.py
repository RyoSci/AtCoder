import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = dict()
for i in range(n):
    s = input().strip()
    if s not in d:
        d[s] = 0
    d[s] += 1

res = 0
ans = ""
for key, val in d.items():
    if res < val:
        res = val
        ans = key

print(ans)
