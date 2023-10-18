# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = list(map(int, input().split()))
a = []
a.append(s[0])

for i in range(n-1):
    a.append(s[i+1]-s[i])

print(*a)
