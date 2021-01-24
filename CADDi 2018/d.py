n = int(input())
ans = "second"
for i in range(n):
    if int(input()) % 2 == 1:
        ans = "first"

print(ans)
