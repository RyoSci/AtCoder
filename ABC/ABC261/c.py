# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
d = dict()
ans = []
for i in range(n):
    s = input()
    if s not in d:
        ans.append(s)
        d[s] = 0
    else:
        ans.append(f"{s}({d[s]})")
    d[s] += 1

print(*ans)
