sx, sy, gx, gy = map(int, input().split())
res = (gy * sx + gx * sy) / (gy + sy)
print(res)
