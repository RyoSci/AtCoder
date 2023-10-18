# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
w = list(map(str, input().split()))

s = {"and", "not", "that", "the", "you"}

for i in range(n):
    if w[i] in s:
        print("Yes")
        exit()
else:
    print("No")
