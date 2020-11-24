r, g, b, n = map(int, input().split())

ans = 0
for i in range(3001):
    for j in range(3001):
        rest = n - r * i - g * j
        if rest % b == 0 and 0 <= rest // b <= 3000:
            ans += 1

print(ans)
