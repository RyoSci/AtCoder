import math
n, X = map(int, input().split())
x = list(map(int, input().split()))
X_x = [0] * n

for i in range(n):
    X_x[i] = abs(x[i] - X)

gcd = X_x[0]
for i in range(1, n):
    gcd = math.gcd(gcd, X_x[i])

print(gcd)