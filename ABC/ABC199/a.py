a, b, c = map(int, input().split())

if a ** 2 + b ** 2 < c ** 2:
    ans = "Yes"
else:
    ans = "No"

print(ans)
