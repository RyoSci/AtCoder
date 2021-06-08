import math as m

a, b, x = map(int, input().split())

if a*b*a >= 2*x:
    sita = m.atan(a*b*b/(2*x))
else:
    sita = m.atan((2*a**2*b-2*x)/a**3)

print(m.degrees(sita))
