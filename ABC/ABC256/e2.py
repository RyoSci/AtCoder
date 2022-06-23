# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
x = list(map(lambda x: int(x)-1, input().split()))
c = list(map(int, input().split()))

seen = [0]*n
finished = [0]*n


def dfs(par, root=-1):
    seen[par] = 1
    hist.append(par)
    chi = x[par]
    ans = 0
    if finished[chi]:
        pass
    elif seen[chi] and not finished[chi]:
        res = INF
        while len(hist) > 0:
            tmp = hist.pop()
            res = min(res, c[tmp])
            if tmp == chi:
                break
        ans += res
    else:
        ans += dfs(chi, par)
    finished[par] = 1
    return ans


ans = 0
for i in range(n):
    if seen[i]:
        continue
    hist = []
    ans += dfs(i)

print(ans)
