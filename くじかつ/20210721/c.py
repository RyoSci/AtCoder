from math import atan, degrees
a, b, x = map(int, input().split())

if 2*x <= a*a*b:
    sita = atan(a*b*b/2/x)
else:
    sita = atan(2*(a*a*b-x)/(a**3))

print(degrees(sita))
