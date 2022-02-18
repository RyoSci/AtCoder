a, b = map(int, input().split())

mul = 2 ** 0
ans = 0
while 1:
    tmp = (b + 1) // (mul * 2) * mul + max(0, (b + 1) % (mul * 2) - mul)
    tmp -= (a) // (mul * 2) * mul + max(0, (a) % (mul * 2) - mul)
    ans += (tmp % 2) * mul
    mul *= 2
    if mul > 10 ** 12:
        break
print(ans)
