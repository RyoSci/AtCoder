# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))

if 0 in a:
    print(0)
    exit()

res = 1
for i in a:
    if res*i > INF:
        res = -1
        break
    res *= i

print(res)
