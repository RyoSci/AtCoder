n = int(input())
k = int(input())
x = int(input())
y = int(input())

res = min(n, k) * x + (n - min(n, k)) * y
print(res)
