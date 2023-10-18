# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

p, q = map(str, input().split())
ag = [0, 3, 4, 8, 9, 14, 23]

ans = abs(ag[ord(p)-ord("A")]-ag[ord(q)-ord("A")])
print(ans)
