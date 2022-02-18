x1, y1, x2, y2 = map(int, input().split())
ab = (x2 - x1, y2 - y1)
bc = (- ab[1], ab[0])

print(x2 + bc[0], y2 + bc[1], x1 + bc[0], y1 + bc[1])