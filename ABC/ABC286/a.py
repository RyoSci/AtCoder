# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
tmp = a[p-1:q][::]
a[p-1:q] = a[r-1:s][::]
a[r-1:s] = tmp
print(*a)
