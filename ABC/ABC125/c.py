# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

# n = 10**5
# a = [10**9-_ for _ in range(n)]


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)


# tot = 1
# for i in range(n):
#     # tot *= a[i]
#     tot = lcm(tot, a[i])

# l = [tot]*(n+1)
# r = [tot]*(n+1)
l = [0]*(n+1)
r = [0]*(n+1)


for i in range(n):
    l[i+1] = gcd(l[i], a[i])

for i in range(n, 0, -1):
    r[i-1] = gcd(r[i], a[i-1])

ans = 1
for i in range(n):
    ans = max(ans, gcd(l[i], r[i+1]))

print(ans)
