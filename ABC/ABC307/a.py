# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    res = 0
    for j in range(7):
        res += a[i*7+j]
    ans.append(res)

print(*ans)
