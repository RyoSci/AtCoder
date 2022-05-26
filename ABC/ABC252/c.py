# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = [input() for _ in range(n)]

ans = INF
for i in range(10):
    seen = set()
    for j in range(n):
        tmp = s[j].find(str(i))
        while 1:
            if tmp not in seen:
                seen.add(tmp)
                break
            tmp += 10
    ans = min(ans, max(list(seen)))

print(ans)
