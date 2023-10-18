# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
s = input()


m = [[] for _ in range(3)]
x = [[] for _ in range(3)]

for i in range(n):
    if s[i] == "M":
        m[a[i]].append(i)
    elif s[i] == "X":
        x[a[i]].append(i)


ans = 0
for j in range(n):
    if s[j] == "E":
        for ai in range(3):
            for ak in range(3):
                l = bisect_left(m[ai], j)
                r = len(x[ak]) - bisect_left(x[ak], j)

                tot = {0, 1, 2, 3}
                tmp = {ai, a[j], ak}
                tmp = tot-tmp
                tmp = min(tmp)

                ans += l*r*tmp
print(ans)
