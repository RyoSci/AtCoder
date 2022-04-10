# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


dq = deque()

ans = []
q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1:]
        dq.append([x, c])
    else:
        c = query[1]
        now = 0
        cnt = 0
        while 1:
            xx, cc = dq.popleft()
            use = min(cc, c-cnt)
            cc -= use
            cnt += use
            now += xx*use
            if cc > 0:
                dq.appendleft([xx, cc])
            if cnt == c:
                break
        ans.append(now)

print(*ans, sep="\n")
