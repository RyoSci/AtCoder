x, y, a, b = map(int, input().split())
res = x
for i in range(0, 70):
    if y <= res * a or res * a > res + b:
        break
    res *= a

counter = i
counter += max(0, y - res - 1) // b

print(counter)
