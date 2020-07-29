import math
a, b, c, d = map(int, input().split())

c_f = (a + c - 1) // c
c_e =  b // c
d_f = (a + d - 1) // d
d_e =  b // d

cd = c * d // math.gcd(c, d)
c_d_num = b // cd - (a + cd - 1) // cd + 1

num = b - a + 1 - (c_e - c_f + 1 + d_e - d_f + 1 - c_d_num)
 
print(num)