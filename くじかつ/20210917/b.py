from decimal import *
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

x = int(input())
n = 100
for i in range(10**5):
    if n >= x:
        res = i
        break
    n = n+int(Decimal(n)*Decimal("0.01"))

print(res)
