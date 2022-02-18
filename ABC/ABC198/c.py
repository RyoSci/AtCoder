import math

r, x, y = map(int, input().split())

if x ** 2 + y ** 2 < r ** 2:
    ans = 2
else:
    ans = (x ** 2 + y ** 2)**(1 / 2) / r
    ans = math.ceil(ans)
    
print(ans)