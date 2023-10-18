# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(si)

s = s[:k]
s.sort()

print(*s, sep="\n")
