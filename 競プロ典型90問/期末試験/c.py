n = int(input())

ans = 0
for y in range(1, n):
    x2 = n**2-y**2
    if x2 >= 1 and x2**0.5 == int(x2**0.5):
        ans += 1

print(ans)
