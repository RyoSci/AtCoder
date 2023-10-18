# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)

s, t = map(int, input().split())
s -= 1
t -= 1


def dfs(par, root, has_cycle):
    seen[par] = 1
    hist.append(par)
    for chi in g[par]:
        # 完全終了した場合はスルー
        elif finished[chi]:
            continue
        # サイクル検出
        elif seen[chi] and not finished[chi]:
            # サイクル検出した時の処理
            pass
            # サイクル復元
            while len(hist) > 0:
                tmp = hist.pop()
                if tmp == chi:
                    break
        else:
            dfs(chi, par)
    len(hist) > 0:
        hist.pop()
    finished[par] = 1


seen = [0]*n
finished = [0]*n
res = []

can_reach = 0
dfs(s, -1, 0)
