import math
t = int(input())
l, x, y = map(int, input().split())
q = int(input())

for i in range(q):
    e = int(input())
    sita = e/t*2*math.pi
    yy = -l/2*math.sin(sita)
    zz = l/2*(-math.cos(sita)+1)
    print(math.atan(zz/(math.sqrt(x**2+(y-yy)**2)))/math.pi*180)
