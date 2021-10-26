import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b, c = map(int, input().split())

mod = 998244353


def cal(x):
    return x*(x+1)//2 % mod


res = 1
res *= cal(a)
res %= mod
res *= cal(b)
res %= mod
res *= cal(c)
res %= mod

print(res)
