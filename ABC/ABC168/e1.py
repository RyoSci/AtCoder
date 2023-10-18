# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

ans = 0
mod = 10**9+7
for i in range(1 << n):
    use = []
    for j in range(n):
        if i >> j & 1:
            use.append(j)

    flag = True
    for j in range(len(use)-1):
        for k in range(j+1, len(use)):
            if a[use[j]]*a[use[k]] + b[use[j]]*b[use[k]] == 0:
                flag = False
                break
        if not flag:
            break

    if flag:
        ans += 1
        ans %= mod

ans -= 1
print(ans % mod)
