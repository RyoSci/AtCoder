# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
ans = 0
for i in s:
    if i == "v":
        ans += 1
    else:
        ans += 2

print(ans)
