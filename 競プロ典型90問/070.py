n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

x_ = x[n//2]
y_ = y[n//2]

res = 0
for i in range(n):
    res += abs(x[i]-x_)
    res += abs(y[i]-y_)

print(res)
