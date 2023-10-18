# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
n = len(s)
ans = 1
for i in range(n):
    for j in range(i+1, n):
        t = s[i:j+1]
        if t == t[::-1]:
            ans = max(ans, len(t))


print(ans)
