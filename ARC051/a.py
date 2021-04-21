x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

red = "YES"
blue = "YES"
if x3 - x1 >= r and x1 - x2 >= r and y3 - y1 >= r and y1 - y2 >= r:
    red = "NO"
else:
    is_break = False
    for x in [x2, x3]:
        for y in [y2, y3]:
            if (x - x1) ** 2 + (y - y1) ** 2 > r ** 2:
                is_break = True
                break
        if is_break:
            break
    else:
        blue = "NO"

print(red, blue, sep="\n")
