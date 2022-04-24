# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
t = list(map(int, input().split()))

pre = 0
for i in range(n):
    now = 1 << t[i]
    if pre < now:
        pre = now
    else:
        if pre >> t[i] & 1:
            pre = pre >> t[i]
            pre += 2
            pre = pre << t[i]
        else:
            pre = pre >> t[i]
            pre += 1
            pre = pre << t[i]

print(pre)
