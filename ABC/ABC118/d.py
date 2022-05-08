# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18

n, m = map(int, input().split())
a = list(map(int, input().split()))
# n = 10**4
# m = 9
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

use = [INF, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [[0]*10 for _ in range(n+1)]

dp[0][0] = 1


def f(a, b):
    update = False
    cnt_a = sum(a)
    cnt_b = sum(b)

    if cnt_a < cnt_b:
        update = True
    elif cnt_a == cnt_b:
        for i in range(9, -1, -1):
            if a[i] == b[i]:
                continue
            elif a[i] < b[i]:
                update = True
                break
            else:
                break

    return update


for i in range(m):
    for j in range(n+1):
        tmp = dp[j][::]
        if sum(tmp) == 0:
            continue
        # 使う場合
        tmp[a[i]] += 1
        nj = j+use[a[i]]
        if nj <= n:
            if f(dp[nj], tmp):
                dp[nj] = tmp[::]

# print(dp[n])

ans = ""
for i in range(9, 0, -1):
    ans += str(i)*dp[n][i]

print(ans)
