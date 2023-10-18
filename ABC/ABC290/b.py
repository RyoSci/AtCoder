# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
s = input()

ans = ""

for i in range(n):
    if k > 0 and s[i] == "o":
        ans += "o"
        k -= 1
    else:
        ans += "x"

print(ans)
