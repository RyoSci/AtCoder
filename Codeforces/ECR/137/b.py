# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
# sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()
# INF = 10**18


t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1]
    for i in range(n, 1, -1):
        ans.append(i)
    print(*ans)
