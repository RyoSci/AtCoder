n, m, k = map(int, input().split())

ans = "No"
for i in range(m + 1):
    for j in range(n + 1):
        num = n * i + (m - 2 * i) * j
        if num == k:
            ans = "Yes"
            break
    if ans == "Yes":
        break

print(ans)
