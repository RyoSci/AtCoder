# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

same_y = dict()
for i in range(n):
    x, y = map(int, input().split())
    if y not in same_y:
        same_y[y] = []
    same_y[y].append([i, x])

s = input().strip()

ans = "No"
for y, i_s in same_y.items():
    l = []
    r = []
    for i, x in i_s:
        if s[i] == "L":
            l.append(x)
        else:
            r.append(x)
    if len(r)*len(l) >= 1 and min(r) < max(l):
        ans = "Yes"
        break

print(ans)
