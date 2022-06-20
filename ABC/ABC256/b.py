# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
masu = [0]*4
p = 0
for i in range(n):
    masu[0] += 1
    for j in range(3, -1, -1):
        if j+a[i] > 3:
            p += masu[j]
        else:
            masu[j+a[i]] += masu[j]
        masu[j] = 0

print(p)
