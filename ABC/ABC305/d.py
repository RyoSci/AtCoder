# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_right
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

tot = [0]
for i in range(1, n):
    if i % 2 == 0:
        tmp = a[i] - a[i-1]
        tot.append(tot[-1]+tmp)
    else:
        tot.append(tot[-1])


q = int(input())
ans = []
for i in range(q):
    l, r = map(int, input().split())
    li = bisect_right(a, l)
    ri = bisect_right(a, r)
    li -= 1
    ri -= 1

    res = tot[ri] - tot[li]
    if ri > 0 and ri % 2 == 1:
        res += r-a[ri]

    if li > 0 and li % 2 == 1:
        res -= l-a[li]

    ans.append(res)

print(*ans)

# print(a)
# print(tot)
