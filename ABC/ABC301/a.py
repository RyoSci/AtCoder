# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

a = 0
t = 0
for si in s:
    if si == "A":
        a += 1
    else:
        t += 1
if a > t:
    print("A")
elif a < t:
    print("T")
else:
    m = a
    a = 0
    t = 0
    for si in s:
        if si == "A":
            a += 1
            if a == m:
                print("A")
                exit()
        else:
            t += 1
            if t == m:
                print("T")
                exit()
