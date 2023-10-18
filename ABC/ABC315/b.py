# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

m = int(input())
d = list(map(int, input().split()))

e = (sum(d) + 1)//2

now = 0
for i in range(m):
    for j in range(d[i]):
        now += 1
        if now == e:
            print(i+1, j+1)
            exit()
