# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

s = list(input())
t = list("atcoder")
n = len(s)

ans = 0
for i in range(n):
    if s[i] == t[i]:
        continue
    else:
        for j in range(i, n):
            if t[i] == s[j]:
                end = j
                break
        for j in range(end, i, -1):
            s[j], s[j-1] = s[j-1], s[j]
            ans += 1

print(ans)
