# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()
t = set()
x = 0
y = 0
t.add((x, y))

for si in s:
    if si == "R":
        x += 1
    if si == "L":
        x -= 1
    if si == "U":
        y -= 1
    if si == "D":
        y += 1

    if (x, y) in t:
        print("Yes")
        exit()
    t.add((x, y))

print("No")
