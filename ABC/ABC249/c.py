# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, k = map(int, input().split())
s = []
for i in range(n):
    # 文字列入力の時は空白区切りでないかチェック
    si = input()
    s.append(si)

ans = 0
for i in range(1 << n):
    use = []
    for j in range(n):
        if i >> j & 1:
            use.append(j)
    d = dict()
    for j in use:
        for c in s[j]:
            if c not in d:
                d[c] = 0
            d[c] += 1
    cnt = 0
    for val in d.values():
        if val == k:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
