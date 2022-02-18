import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = []
t = []
for i in range(n):
    tt, k, *aa = list(map(int, input().split()))
    t.append(tt)
    a.append(aa)


cnt = set()
cnt.add(n-1)


def dfs(x):
    if x == 0:
        return 0
    for chi in a[x]:
        if chi-1 in cnt:
            continue
        cnt.add(chi-1)
        dfs(chi-1)


dfs(n-1)
res = 0
for i in cnt:
    res += t[i]

print(res)
