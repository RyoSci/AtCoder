# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())


# ans = ""
ans = []


def dfs(cnt, s):
    global ans
    if cnt == n:
        return
    # ans = ans+str(cnt+1)+ans
    ans = ans+[cnt+1] + ans
    dfs(cnt+1, ans)


dfs(0, ans)
# ans = list(ans)
# print(*ans, sep=" ")
print(*ans, sep=" ")
