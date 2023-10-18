# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = []
for i in range(n-1):
    di = list(map(int, input().split()))
    d.append(di)

ans = 0
used = [0]*n


def dfs(i, now=0):
    global ans

    ans = max(ans, now)

    if i == n:
        return

    dfs(i+1, now)

    for j in range(i+1, n):
        if used[j] or used[i]:
            continue

        used[i] = 1
        used[j] = 1
        dfs(i+1, now+d[i][j-i-1])
        used[i] = 0
        used[j] = 0


dfs(0)
print(ans)
