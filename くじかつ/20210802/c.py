a, b, n = map(int, input().split())

if n >= b-1:
    x = b-1
else:
    x = n

res = a*x//b-a*int(x/b)
print(res)
