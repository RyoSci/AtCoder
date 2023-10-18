# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())

n2 = ""
while n > 0:
    n2 += str(n % 2)
    n //= 2
n2 = n2[::-1]

m = len(n2)
use = []
for i in range(m):
    if n2[i] == "1":
        use.append(i)

l = len(use)
if l != 0:
    ans = []
    for i in range(1 << l):
        res = ["0"]*m
        for j in range(l):
            if i >> j & 1:
                res[use[j]] = "1"
        res = "".join(res)
        ans.append(int(res, 2))

    ans.sort()
    print(*ans, sep="\n")
else:
    print(0)
