# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

a = list(input())
b = list(input())

for i in range(1, n):
    if int(a[0]) > int(b[0]):
        if int(a[i]) < int(b[i]):
            a[i], b[i] = b[i], a[i]
    else:
        if int(a[i]) > int(b[i]):
            a[i], b[i] = b[i], a[i]
mod = 998244353
a_mod = 0
b_mod = 0
for i in range(n-1, -1, -1):
    a_mod += pow(10, i, mod)*int(a[n-1-i])
    a_mod %= mod
    b_mod += pow(10, i, mod)*int(b[n-1-i])
    b_mod %= mod

print(a_mod*b_mod % mod)
