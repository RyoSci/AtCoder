import math
n, k = map(int, input().split())
a = []
mod = 998244353
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

max_cnt = 0
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            pass
        else:
            for col in range(n):
                if a[col][i] + a[col][j] > k:
                    break
            else:
                cnt += 1
    max_cnt = max(max_cnt, cnt)

max_cnt1 = 0
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            pass
        else:
            for row in range(n):
                if a[i][row] + a[j][row] > k:
                    break
            else:
                cnt += 1
    max_cnt1 = max(max_cnt1, cnt)

ans = 1
for i in range(1, max_cnt + 1):
    ans = (i * ans) % mod

for i in range(1, max_cnt1 + 1):
    ans = (i * ans) % mod

print(ans)
print(max_cnt, max_cnt1)
print(math.factorial(10) ** 2 % mod)
