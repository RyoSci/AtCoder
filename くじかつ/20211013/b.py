import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())
a, b = map(int, input().split())


def f(x):
    res = 0
    x = str(x)
    n = len(x)
    for i in range(n):
        res += k**(n-i-1)*int(x[i])
    return int(res)


print(f(a)*f(b))
