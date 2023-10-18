# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, t = map(int, input().split())
a = list(map(int, input().split()))
tot = sum(a)

t %= tot

for i in range(n):
    if t <= a[i]:
        print(i+1, t)
        exit()
    else:
        t -= a[i]
