# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

N, A, B = list(map(int, input().split()))


def f(x):
    return x*(x+1)//2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)


l = lcm(A, B)

ans = f(N)-f(N//A)*A-f(N//B)*B+f(N//l)*l
print(ans)
