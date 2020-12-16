n, k = map(int, input().split())
a = list(map(int, input().split()))
a_sum = [0] * (n + 1)
for i in range(n):
    a_sum[i + 1] = a_sum[i] + a[i]

l = 0
ans = 0
for r in range(n):
    while a_sum[r + 1] - a_sum[l] >= k:
        ans += n - r
        l += 1

print(ans)
