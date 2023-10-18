# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


INF = 10**18
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for i in range(m):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1
        g[ui].append((vi, i))
        g[vi].append((ui, 2010+i))

    dp = [[INF]*n for _ in range(n)]
    dp[0][n-1] = 0

    q = deque()
    q.append((0, n-1))

    # seen = [[0]*4100 for _ in range(4100)]
    # seen = set()
    while len(q) > 0:
        taka, aoki = q.popleft()

        for ntaka, i in g[taka]:
            for naoki, j in g[aoki]:
                if c[ntaka] == c[naoki]:
                    continue
                # if seen[i][j]:
                # if (i, j) in seen:
                #     continue
                if dp[ntaka][naoki] > dp[taka][aoki]+1:
                    # seen[i][j] = 1
                    # seen.add((i, j))
                    dp[ntaka][naoki] = dp[taka][aoki]+1
                    q.append((ntaka, naoki))

    if dp[n-1][0] == INF:
        print(-1)
    else:
        print(dp[n-1][0])
