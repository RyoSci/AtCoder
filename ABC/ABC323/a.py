# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18


s = input()
n = len(s)

ans = "Yes"
for i in range(n):
    if i % 2 == 1:
        if s[i] == "0":
            pass
        else:
            ans = "No"

print(ans)
