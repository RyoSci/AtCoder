# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


def f(n):
    res = ""
    while(n > 0):
        res += str(n % 9)
        n //= 9
    return res[::-1]


n, k = map(int, input().split())
for i in range(k):
    n = int(str(n), 8)
    n = f(n)
    n = n.replace("8", "5")
    if n == "":
        n = 0

print(n)
