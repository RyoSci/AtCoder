# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = input()

for i in range(1, n):
    l = 0
    for k in range(n):
        if k+i < n and s[k] != s[k+i]:
            l = k+1
        else:
            break
    print(l)
