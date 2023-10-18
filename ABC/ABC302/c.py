# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(si)

ans = False
for ss in permutations(s):
    ok = True
    for i in range(n-1):
        cnt = 0
        for j in range(m):
            if ss[i][j] == ss[i+1][j]:
                cnt += 1
        if cnt >= m-1:
            continue
        else:
            ok = False
    if ok:
        print("Yes")
        exit()
else:
    print("No")
