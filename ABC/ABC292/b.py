# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, q = map(int, input().split())
cnt = [0]*n
for i in range(q):
    num, x = map(int, input().split())
    x -= 1
    if num == 1:
        cnt[x] += 1
    elif num == 2:
        cnt[x] += 2
    else:
        if cnt[x] >= 2:
            print("Yes")
        else:
            print("No")
