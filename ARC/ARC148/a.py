# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = 0
for i in a[1:]:
    dis = i-a[0]
    g = gcd(g, dis)

if g == 1:
    print(2)
else:
    print(1)
