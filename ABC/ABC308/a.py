# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = list(map(int, input().split()))

ans = "Yes"
n = len(s)
for i in range(n-1):
    if s[i] > s[i+1]:
        ans = "No"

for i in range(n):
    if s[i] < 100 or s[i] > 675:
        ans = "No"

    if s[i] % 25 != 0:
        ans = "No"


print(ans)
