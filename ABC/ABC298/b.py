# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

b = []
for i in range(n):
    tmp = list(map(int, input().split()))
    b.append(tmp)


def rot(a):
    na = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            na[n-1-j][i] = a[i][j]
    return na


for i in range(4):

    ans = "Yes"
    for j in range(n):
        for k in range(n):
            if a[j][k] == 1:
                if b[j][k] == 0:
                    ans = "No"

    if ans == "Yes":
        print(ans)
        exit()
    a = rot(a)
print("No")
