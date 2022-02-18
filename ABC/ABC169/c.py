# a,b=input().split()
# a=int(a)
# b=float(b)
# b_int=int(b)
# b_float=b-b_int

# res=a*b_int+a*b_float
# print(int(res))

from decimal import *
a,b=map(Decimal,input().split())
res=a*b
res=res.quantize(exp=Decimal('1.'),rounding=ROUND_DOWN)
print(res)
