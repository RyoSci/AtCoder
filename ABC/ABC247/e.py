# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

sec = []
l = 0
r = 0
min_a = INF
max_a = 0
while l < n:
    while r < n:
        if y <= a[r] <= x:
            min_a = min(min_a, a[r])
            max_a = max(max_a, a[r])
            r += 1
        else:
            break
    if min_a == y and max_a == x:
        sec.append([l, r-1])
    l = r+1
    r = l
    min_a = INF
    max_a = 0

# print(sec)

xpos = []
ypos = []

for l, r in sec:
    xpos_ = []
    ypos_ = []
    for j in range(l, r+1):
        if a[j] == x:
            xpos_.append(j)
        if a[j] == y:
            ypos_.append(j)
    xpos.append(xpos_)
    ypos.append(ypos_)

ans = 0
for i, (l, r) in enumerate(sec):
    xpos_ = xpos[i]
    ypos_ = ypos[i]
    for j in range(l, r+1):
        min_pos = bisect_left(ypos_, j)
        max_pos = bisect_left(xpos_, j)
        if min_pos < len(ypos_) and max_pos < len(xpos_):
            ans += r-max(ypos_[min_pos], xpos_[max_pos])+1

print(ans)
