# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m, h, k = map(int, input().split())
s = input()

ene = dict()
for i in range(m):
    x, y = map(int, input().split())
    ene[(x, y)] = 1


hp = h
x = 0
y = 0
for i in range(n):

    if s[i] == "R":
        x += 1
    if s[i] == "L":
        x -= 1
    if s[i] == "U":
        y += 1
    if s[i] == "D":
        y -= 1

    hp -= 1

    if hp < 0:
        print("No")
        exit()

    if (x, y) in ene and ene[(x, y)] == 1 and hp < k:
        hp = k
        ene[(x, y)] = 0


else:
    print("Yes")
