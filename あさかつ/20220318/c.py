# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18

x, y = map(int, input().split())

ans = INF
# 4パターン試す
if x <= y:
    ans = min(ans, y-x)

if -x <= y:
    ans = min(ans, y-(-x)+1)

if x <= -y:
    ans = min(ans, -y-x+1)

if -x <= -y:
    ans = min(ans, -y-(-x)+2)

print(ans)
