xa, ya, xb, yb, xc, yc = map(int, input().split())
abc = sorted([[xa, ya], [xb, yb], [xc, yc]])
a = (abc[2][1] - abc[0][1]) / (abc[2][0] - abc[0][0])
b = abc[2][1] - a * abc[2][0]

h = abs(abc[1][1] - (a * abc[1][0] + b))
print(h * (abc[2][0] - abc[0][0]) / 2)
