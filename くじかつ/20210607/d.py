from math import sin, cos, radians
n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

a, b = x0-xn2, y0-yn2
sita = radians(180-((n-2)*180//n/2+90))
cossita = cos(sita)
sinsita = sin(sita)

A = (a**2+b**2)**0.5
B = A*cossita

x1 = (a*cossita-b*sinsita)*cossita
y1 = (b*cossita+a*sinsita)*cossita

print(xn2+x1, yn2+y1)
