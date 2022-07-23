# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
a = []
for i in range(n):
    s = list(input())
    a.append(s)

ans = "correct"
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "W" and a[j][i] == "L":
            continue
        elif a[i][j] == "L" and a[j][i] == "W":
            continue
        elif a[i][j] == "D" and a[j][i] == "D":
            continue
        else:
            ans = "incorrect"

print(ans)
