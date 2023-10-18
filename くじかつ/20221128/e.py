# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations, permutations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, a, b, c = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))


ans = INF
for ijk in combinations(range(1, n+1), 3):
    i, j, k = ijk
    for ll in permutations(l):
        aa = 0
        bb = 0
        cc = 0
        res = 0
        for pos in range(n):
            if pos < i:
                aa += ll[pos]
            elif pos < j:
                bb += ll[pos]
            elif pos < k:
                cc += ll[pos]

        res += (i-1)*10+(j-i-1)*10+(k-j-1)*10
        res += abs(a-aa)+abs(b-bb)+abs(c-cc)
        ans = min(ans, res)

print(ans)
