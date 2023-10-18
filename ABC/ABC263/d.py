# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, l, r = map(int, input().split())
a = list(map(int, input().split()))

if l < r:
    tot = [0]*(n+1)
    for i in range(n):
        tot[i+1] = tot[i]+a[i]
    li = 0
    l_dis = INF
    for i in range(n+1):
        if l_dis > l*i-tot[i]:
            l_dis = l*i-tot[i]
            li = i

    for i in range(li):
        a[i] = l

    a = a[::-1]
    tot = [0]*(n+1)
    for i in range(n):
        tot[i+1] = tot[i]+a[i]

    ri = 0
    r_dis = INF
    for i in range(n+1):
        if r_dis > r*i-tot[i]:
            r_dis = r*i-tot[i]
            ri = i

    for i in range(ri):
        a[i] = r

    print(sum(a))

else:

    a = a[::-1]
    tot = [0]*(n+1)
    for i in range(n):
        tot[i+1] = tot[i]+a[i]

    ri = 0
    r_dis = INF
    for i in range(n+1):
        if r_dis > r*i-tot[i]:
            r_dis = r*i-tot[i]
            ri = i

    for i in range(ri):
        a[i] = r

    a = a[::-1]
    tot = [0]*(n+1)
    for i in range(n):
        tot[i+1] = tot[i]+a[i]

    l_dis = INF
    for i in range(n+1):
        if l_dis > l*i-tot[i]:
            l_dis = l*i-tot[i]
            li = i

    for i in range(li):
        a[i] = l

    print(sum(a))
