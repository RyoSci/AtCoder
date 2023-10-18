# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = input()
ans = ""
for i in s:
    if i == "0":
        ans += "1"
    else:
        ans += "0"

print(ans)
