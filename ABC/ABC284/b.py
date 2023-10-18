# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for j in a:
        if j % 2 == 1:
            ans += 1
    print(ans)
