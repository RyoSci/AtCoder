# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

l, n1, n2 = map(int, input().split())
a = []
l = 0
for i in range(n1):
    v, r = map(int, input().split())
    a.append((v, l, l+r-1))
    l += r

b = []
l = 0
for i in range(n2):
    v, r = map(int, input().split())
    b.append((v, l, l+r-1))
    l += r

j = 0
ans = 0
for i in range(n1):
    vi, li, ri = a[i]
    while j < n2:
        vj, lj, rj = b[j]

        if vi == vj:
            ans += min(ri, rj) - max(li, lj) + 1

        if rj < ri:
            j += 1
        elif rj == ri:
            j += 1
            break
        else:
            break

print(ans)
