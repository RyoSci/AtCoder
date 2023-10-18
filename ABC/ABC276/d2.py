# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
# n = 1000
# a = [2**20*3**10 for i in range(n)]


def counter(ai):
    two = 0
    thr = 0
    while 1:
        if ai % 2 != 0 and ai % 3 != 0:
            break
        if ai % 2 == 0:
            ai //= 2
            two += 1
        elif ai % 3 == 0:
            ai //= 3
            thr += 1
    return ai, two, thr


rest = set()
for i in range(n):
    ai = a[i]
    ai, _, _ = counter(ai)

    rest.add(ai)

if len(rest) > 1:
    print(-1)
    exit()

r = rest.pop()


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = a[0]
for i in range(n):
    a[i] //= r
    g = gcd(g, a[i])


_, two, thr = counter(g)

ans = 0
for i in range(n):
    ai = a[i]
    _, tmp_two, tmp_thr = counter(ai)
    ans += tmp_two-two
    ans += tmp_thr-thr

print(ans)
