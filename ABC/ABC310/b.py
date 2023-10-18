# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
p = []
c = []
f = []
for i in range(n):
    pi, ci, *fi = list(map(int, input().split()))
    fi = set(fi)
    p.append(pi)
    c.append(ci)
    f.append(fi)


for i in range(n):
    for j in range(n):
        if p[i] >= p[j]:
            flag = True
            for fi in f[i]:
                if fi not in f[j]:
                    flag = False
                    break
            if flag:
                tmp = f[j]-f[i]
                if p[i] > p[j] or len(tmp) > 0:
                    print("Yes")
                    exit()
print("No")
