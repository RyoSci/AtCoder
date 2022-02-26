import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ad = dict()
bd = dict()

for i in range(n):
    if a[i] not in ad:
        ad[a[i]] = 0
    ad[a[i]] += 1

for i in range(m):
    if b[i] not in bd:
        bd[b[i]] = 0
    bd[b[i]] += 1

ans = "Yes"
for key, val in bd.items():
    if key in ad and ad[key] >= val:
        continue
    else:
        ans = "No"

print(ans)
