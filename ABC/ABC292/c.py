# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from math import sqrt
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

d = [0]*(n+1)

for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if j*j > i:
            break
        if i % j == 0:
            if i//j == j:
                cnt += 1
            else:
                cnt += 2
    d[i] = cnt

ans = 0
for a in range(1, int(sqrt(n))+1):
    for b in range(a, n//a+1):
        if a*b >= n:
            break

        if a == b:
            cnt = 1
        else:
            cnt = 2

        cd = n-a*b
        ans += d[cd]*cnt

        # for c in range(1, cd+1):
        #     if c*c > cd:
        #         break
        #     if cd % c == 0:
        #         if cd//c == c:
        #             ans += cnt*1
        #         else:
        #             ans += cnt*2

print(ans)
