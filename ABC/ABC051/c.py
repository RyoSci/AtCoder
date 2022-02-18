sx, sy, tx, ty = map(int, input().split())
st1 = "U" * (ty - sy) + "R" * (tx - sx)
ts1 = "D" * (ty - sy) + "L" * (tx - sx)
st2 = "L" + "U" * (ty - sy + 1) + "R" * (tx - sx + 1) + "D"
ts2 = "R" + "D" * (ty - sy + 1) + "L" * (tx - sx + 1) + "U"

print(st1 + ts1 + st2 + ts2)
