# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

for x in range(100):
    for y in range(100):
        xy = (2**x) * (3**y)

        if xy == n:
            print("Yes")
            exit()
        elif xy > n:
            break
print("No")
