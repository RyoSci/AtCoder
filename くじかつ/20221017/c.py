# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = dict()
for i in "MARCH":
    d[i] = 0

for i in range(n):
    s = input()
    if s[0] in d:
        d[s[0]] += 1


ans = 0
for i in combinations("MARCH", 3):
    tmp = 1
    for j in i:
        tmp *= d[j]
    ans += tmp
print(ans)
