# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from copy import deepcopy
from itertools import permutations, combinations_with_replacement, combinations
import math
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
t = set(t)
s_num = 0
for i in range(n):
    s_num += len(s[i])

rest = 16-s_num-(n-1)
for i in permutations(s):
    for j in range(0, rest+1):
        for k in combinations_with_replacement(range(n-1), j):
            add = [1]*(n-1)
            for l in k:
                add[l] += 1
            res = i[0]
            for l in range(n-1):
                res += "_"*add[l]
                res += i[l+1]
            if 3 <= len(res) and res not in t:
                # if res not in t:
                print(res)
                exit()
print(-1)
