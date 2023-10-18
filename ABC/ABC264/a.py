# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

l, r = map(int, input().split())
l -= 1
r -= 1

s = "atcoder"
print(s[l:r+1])
