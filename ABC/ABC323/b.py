# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)


tot = []

for i in range(n):
    win = 0
    for j in range(n):
        if s[i][j] == "o":
            win += 1
    tot.append([-win, i+1])


tot.sort()
for i in range(n):
    print(tot[i][-1])
