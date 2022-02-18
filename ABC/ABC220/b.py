import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

k = int(input())
a, b = input().strip().split()


def f(x):
    tmp = 0
    n = len(x)
    for i in range(n):
        tmp += int(x[i])*k**(n-i-1)
    return tmp


print(f(a)*f(b))
