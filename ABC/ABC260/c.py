# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = list(map(int, input().split()))


def dfs(i, cnt, is_red):
    global ans
    if i == 1:
        if not is_red:
            ans += cnt
        return
    if is_red:
        dfs(i-1, cnt, 1)
        dfs(i, cnt*x, 0)
    else:
        dfs(i-1, cnt, 1)
        dfs(i-1, cnt*y, 0)


ans = 0
dfs(n, 1, 1)
print(ans)
