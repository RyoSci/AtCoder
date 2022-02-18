import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x = map(int, input().split())
a = []
for i in range(n):
    l, *ai = map(int, input().split())
    a.append(ai)

ans = 0


def dfs(now_i, res):
    global ans
    if res > x:
        return
    if now_i == n:
        if res == x:
            ans += 1
        return
    for chi in a[now_i]:
        dfs(now_i+1, res*chi)
    return


dfs(0, 1)
print(ans)
