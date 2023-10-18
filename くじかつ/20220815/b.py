# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, m = map(int, input().split())

for i in combinations(range(1, 1+m), n):
    print(*i)
