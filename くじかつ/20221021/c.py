# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
s = []
for i in range(n):
    si = input()
    s.append(list(set(si)))

ans = 0
for i in range(1 << n):
    cnt = dict()
    for j in range(n):
        if i >> j & 1:
            for sj in s[j]:
                if sj not in cnt:
                    cnt[sj] = 0
                cnt[sj] += 1
    tmp = 0
    for key, val in cnt.items():
        if val == k:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
