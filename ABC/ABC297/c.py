# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
s = []
for i in range(h):
    si = input()
    s.append(list(si))

for i in range(h):
    for j in range(w-1):
        if s[i][j] == "T" and s[i][j+1] == "T":
            s[i][j] = "P"
            s[i][j+1] = "C"

for i in range(h):
    print("".join(s[i]))
