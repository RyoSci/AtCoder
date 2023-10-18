# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = list(map(int, input().split()))


def dfs(i, is_red):
    if i == 1:
        if not is_red:
            return 1
        else:
            return 0
    if (i, is_red) in memo:
        return memo[(i, is_red)]
    if is_red:
        tmp = dfs(i-1, 1) + dfs(i, 0)*x
        memo[(i, is_red)] = tmp
        return tmp
    else:
        tmp = dfs(i-1, 1) + dfs(i-1, 0)*y
        memo[(i, is_red)] = tmp
        return tmp


memo = dict()
print(dfs(n, 1))
