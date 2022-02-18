a, b, c, d = map(int, input().split())

if c*d == b:
    res = -1
else:
    if a % (c*d-b) == 0:
        res = a//(c*d-b)
    else:
        res = int(a//(c*d-b))+1

    if res <= 0:
        res = -1
print(res)
