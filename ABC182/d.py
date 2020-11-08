n = int(input())
a = list(map(int, input().split()))
a_sum = [0] * (n + 1)
max_a_sum = 0
max_index = 0
r = 0
for i in range(n):
    a_sum[i + 1] = a[i] + a_sum[i]
    if max_a_sum <= a_sum[i + 1]:
        max_a_sum = a_sum[i + 1]
        max_index = i + 1
    if a_sum[i + 1] >= 0:
        r = i + 1

ans = 0
res = 0
for i in range(r):
    res += a_sum[i + 1]
    ans = max(res, ans)
for i in range(n):
    res += a[i]
    ans = max(res, ans)

print(ans)
