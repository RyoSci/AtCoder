a = [0] * 20
a[0], a[1], a[2] = 100, 100, 200

for i in range(3, 20):
    a[i] = a[i - 1] + a[i - 2] + a[i - 3]

print(a[-1])
