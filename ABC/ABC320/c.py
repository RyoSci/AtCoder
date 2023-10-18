# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from itertools import permutations
import sys
if __file__ != 'prog.py':
    sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().rstrip()


INF = 10**18

m = int(input())
s = []
for i in range(3):
    si = input()
    s.append(list(si))

stop_times = [[[] for j in range(10)] for i in range(3)]

for i in range(3):
    for j in range(m):
        num = int(s[i][j])-1
        stop_times[i][num].append(j)
        stop_times[i][num].append(j+m)
        stop_times[i][num].append(j+m*2)

for i in range(3):
    for j in range(10):
        stop_times[i][j].sort()

# print(*stop_times, sep="\n")
ans = INF
for i in range(10):
    for j in permutations(range(3)):
        now = -1
        flag = True
        for k in j:
            for l in stop_times[k][i]:
                if now < l:
                    now = l
                    break
            else:
                flag = False
        if flag:
            ans = min(ans, now)

if ans == INF:
    print(-1)
else:
    print(ans)
