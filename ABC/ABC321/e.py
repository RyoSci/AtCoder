# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

t = int(input())
# t = 10**5


def pow(a, b):
    ret = 1
    while b > 0:
        if a > INF:
            return INF*2

        if b % 2 == 1:
            ret *= a
            b -= 1

        a = a*a
        b //= 2

    return ret


ans = []
for i in range(t):
    n, x, k = map(int, input().split())
    # n, x, k = (10**18, 10**18, 10**18-1)

    res = 0

    # 下がる
    l = x * pow(2, k)
    r = l + pow(2, k) - 1

    if l <= n:
        res += min(n, r) - l + 1

    # 上がって下がる
    while x != 1 and k > 0:
        k -= 1
        px = x
        x //= 2
        if k == 0:
            res += 1
            break

        nk = k-1
        nx = x*2
        if nx == px:
            if nx % 2 == 1:
                nx -= 1
            else:
                nx += 1

        l = nx * pow(2, nk)
        r = l + pow(2, nk) - 1
        if l <= n:
            res += min(n, r) - l + 1

    ans.append(res)

print(*ans)
