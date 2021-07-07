sx, sy, tx, ty = map(int, input().split())
up = (ty-sy)*"U"+(tx-sx)*"R"
down = (ty-sy)*"D"+(tx-sx)*"L"
a = "LU"
b = "RD"

res = up+down+a+up+b+b+down+a
print(res)
