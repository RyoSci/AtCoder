s, p = map(int, input().split())

ans = "No"
for n in range(1, 10 ** 6 + 1):
    if p % n == 0:
        m = p // n
        if n + m == s:
            ans = "Yes"
            break
print(ans)
