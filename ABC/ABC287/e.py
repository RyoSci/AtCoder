# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n = int(input())
s = []
for i in range(n):
    si = input()
    s.append((si, i))

s.sort()

# print(*s, sep="\n")

ans = [0]*n
for ind in range(n-1):
    si, i = s[ind]
    sj, j = s[ind+1]

    m = min(len(si), len(sj))
    cnt = 0
    for ii in range(m):
        if si[ii] == sj[ii]:
            cnt += 1
        else:
            break

    ans[i] = max(ans[i], cnt)
    ans[j] = max(ans[j], cnt)


print(*ans, sep="\n")
