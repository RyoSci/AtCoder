x, y, a, b = map(int, input().split())

res = x
i = 0
while res < y:
    if res * a > res + b:
        break
    i += 1
    res = x * (a ** i)
else:
    res //= a
    i -= 1

i += max(0, y - res) // b
if (y - res) % b == 0 and i > 0:
    i -= 1
print(i)
