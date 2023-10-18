# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())

n = str(n)


def e2t(x):
    res = 0
    n = len(x)
    x = x[::-1]
    for i in range(n):
        res += int(x[i])*pow(8, i)

    return res


def t2n(x):
    res = ""
    while x > 0:
        tmp = x % 9
        if tmp == 8:
            tmp = 5
        res += str(tmp)
        x //= 9
    return res[::-1]


for i in range(k):
    n = str(n)
    n = e2t(n)
    n = t2n(n)
    if n == "":
        n = 0

print(n)
