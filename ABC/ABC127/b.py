r, d ,x =map(int, input().split())
a = [0] * 11
a[0] = x

for i in range(1, 11):
    a[i] = r * a[i - 1] - d
    print(a[i])
