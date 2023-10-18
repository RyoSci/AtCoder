# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
a = []
b = []
for i in range(h):
    ai = list(input())
    a.append(ai)

for i in range(h):
    bi = list(input())
    b.append(bi)

for s in range(h):
    aa = []
    for i in range(h):
        tmp = []
        for j in range(w):
            tmp.append(a[i][j])
        aa.append(tmp)

    for _ in range(s+1):
        top = []
        for i in range(w):
            top.append(a[h-1][i])

        for i in range(h-1, 0, -1):
            for j in range(w):
                a[i][j] = a[i-1][j]

        for i in range(w):
            a[0][i] = top[i]

    for t in range(w):
        top = []
        for i in range(h):
            top.append(a[i][w-1])

        for i in range(h):
            for j in range(w-1, 0, -1):
                a[i][j] = a[i][j-1]

        for i in range(h):
            a[i][0] = top[i]

        # print("a", a)
        # print("b", b)
        if a == b:
            print("Yes")
            exit()
    a = aa

else:
    print("No")
