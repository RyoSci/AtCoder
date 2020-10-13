n, m = map(int, input().split())
for a in range(10 ** 5 + 1):
    b = m - 2 * n - 2 * a
    c = n - a - b
    if b >= 0 and c >= 0:
        print(c, b, a)
        break
else:
    print(-1, -1, -1)
