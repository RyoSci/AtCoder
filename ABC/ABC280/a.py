# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

h, w = map(int, input().split())

ans = 0
for i in range(h):
    s = input()
    for j in s:
        if j == "#":
            ans += 1

print(ans)
