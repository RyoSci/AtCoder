n = int(input())
ans = min(n // 10 * 100 + (n - n // 10 * 10) * 15, (n + 9) // 10 * 100)
print(ans)
