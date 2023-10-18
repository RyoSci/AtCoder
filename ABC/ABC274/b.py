# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())
c = []
for i in range(h):
    ci = input()
    c.append(ci)

ans = [0]*w
for j in range(w):
    for i in range(h):
        if c[i][j] == "#":
            ans[j] += 1

print(*ans)
