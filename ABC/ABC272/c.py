# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = list(map(int, input().split()))
odd = []
even = []
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

if len(odd) < 2 and len(even) < 2:
    print(-1)
else:
    odd.sort()
    even.sort()
    ans = 0
    if len(odd) >= 2:
        ans = max(ans, odd[-1]+odd[-2])

    if len(even) >= 2:
        ans = max(ans, even[-1]+even[-2])

    print(ans)
