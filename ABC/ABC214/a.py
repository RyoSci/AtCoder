n = int(input())

if 1 <= n <= 125:
    ans = 4
elif 126 <= n <= 211:
    ans = 6
else:
    ans = 8

print(ans)
