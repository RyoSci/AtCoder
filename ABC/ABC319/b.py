# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

ele = []

ans = []
for i in range(n+1):

    for j in range(1, 10):
        if n % j == 0 and i % (n//j) == 0:
            ans.append(str(j))
            break
    else:
        ans.append("-")

print("".join(ans))
