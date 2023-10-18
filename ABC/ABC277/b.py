# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = set()

ans = "Yes"
for i in range(n):
    t = input()
    if t[0] not in {"H", "D", "C", "S"}:
        ans = "No"
    if t[1] not in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}:
        ans = "No"

    s.add(t)

if len(s) != n:
    ans = "No"

print(ans)
