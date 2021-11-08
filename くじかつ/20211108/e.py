import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, A, B, C = list(map(int, input().split()))
l = [int(input()) for _ in range(n)]

res = 10**18


def dfs(i, cost, a, b, c):
    global res
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return
        res = min(res, cost+abs(a-A)+abs(b-B)+abs(c-C))
        return
    if a > 0:
        dfs(i+1, cost+10, a+l[i], b, c)
    else:
        dfs(i+1, cost, a+l[i], b, c)
    if b > 0:
        dfs(i+1, cost+10, a, b+l[i], c)
    else:
        dfs(i+1, cost, a, b+l[i], c)
    if c > 0:
        dfs(i+1, cost+10, a, b, c+l[i])
    else:
        dfs(i+1, cost, a, b, c+l[i])

    dfs(i+1, cost, a, b, c)


dfs(0, 0, 0, 0, 0)

print(res)
