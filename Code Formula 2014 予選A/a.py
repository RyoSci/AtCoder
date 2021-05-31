a = int(input())
ans = "NO"
for i in range(1, 101):
    if a == i**3:
        ans = "YES"

print(ans)
