# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
s = [int(i) for i in s]
s.sort()

ans = 0
for i in range(10**7+10):
    ii = i*i

    ii = str(ii)
    ii = [int(i) for i in ii]

    if len(ii) <= n:
        ii += [0]*(n-len(ii))
    else:
        continue

    ii.sort()

    if ii == s:
        ans += 1

print(ans)
