n, k, m, r = map(int, input().split())
s = sorted([int(input()) for _ in range(n - 1)], reverse=True)

if sum(s[:k]) >= k * r:
    ans = 0
elif k * r - sum(s[:k - 1]) <= m:
    ans = k * r - sum(s[:k - 1])
else:
    ans = -1

print(ans)
