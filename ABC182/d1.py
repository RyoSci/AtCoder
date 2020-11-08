n = int(input())
a = list(map(int, input().split()))
a_sum = [0] * (n + 1)

for i in range(n):
    a_sum[i + 1] = a[i] + a_sum[i]

ans = 0
res = 0
max_a_sum = 0
for i in range(n + 1):
    ans = max(ans, res + max_a_sum)
    if max_a_sum <= a_sum[i]:
        max_a_sum = a_sum[i]
    res += a_sum[i]

ans = max(ans, res)

print(ans)
