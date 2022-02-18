x, y = map(int, input().split())

for l in range(1, 100):
    if 2 ** (l - 1) * x > y:
        l -= 1
        break

print(l)
