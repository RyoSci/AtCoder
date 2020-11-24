r, g, b, n = map(int, input().split())
r, g, b = sorted([r, g, b], reverse=True)
ans = 0
for i in range(n // r + 1):
    for j in range((n - r * i) // g + 1):
        rest = n - r * i - g * j
        if rest % b == 0 and 0 <= rest // b <= 3000:
            ans += 1

print(ans)
