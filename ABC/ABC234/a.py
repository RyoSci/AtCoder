import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


def f(x):
    return x*x+2*x+3


print(f(f(f(t)+t)+f(f(t))))
