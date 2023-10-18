# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())

d = dict()
ans = []
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        d[(a, b)] = 1
    elif t == 2:
        if (a, b) in d:
            d[(a, b)] = 0
    else:
        if (a, b) in d and d[(a, b)] == 1 and (b, a) in d and d[(b, a)]:
            ans.append("Yes")
        else:
            ans.append("No")

print(*ans)
