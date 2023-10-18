# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
# sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()
# INF = 10**18


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    ans = 0
    for x in range(10):
        for y in range(x+1, 10):
            if x not in a and y not in a:
                ans += 6
    print(ans)
