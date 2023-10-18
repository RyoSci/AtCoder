# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
a = []
for i in range(n):
    l, *ai = list(map(int, input().split()))
    a.append(ai)

for i in range(q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    print(a[s][t])
