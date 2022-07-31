# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

a, b = map(int, input().split())

ans = 1
for i in range(a, b):
    for j in range(1, i+1):
        if j*j > i:
            break
        if i % j == 0:
            div = i//j
            if j*(div+1) <= b:
                ans = max(ans, j)
            div = i//(i//j)
            if i//j*(div+1) <= b:
                ans = max(ans, i//j)

print(ans)
