# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b, k = list(map(int, input().split()))

ans = 0
while a < b:
    a *= k
    ans += 1

print(ans)
