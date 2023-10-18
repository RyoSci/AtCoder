# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

k = int(input())

ans = ""

for i in range(k):
    ans += chr(ord("A") + i)

print(ans)
