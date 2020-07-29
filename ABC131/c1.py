import math
a, b, c, d = map(int, input().split())

def f(a, b, c):
    return b // c - (a + c - 1) // c + 1 

c_num = f(a, b, c)
d_num = f(a, b, d)

cp = c
dp = d
mod = 1
while mod > 0:
    mod = cp % dp
    cp = dp
    dp = mod

cd_num =  f(a, b, (c * d) // cp)
print(b - a + 1 - c_num - d_num + cd_num)
