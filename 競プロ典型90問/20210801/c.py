n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

sumx = sum(x)
sumy = sum(y)

resx = 10**18
tmp = 0
for i in range(n):
    tmp += x[i]
    sumx -= x[i]
    resx = min(resx, sumx-tmp-x[i]*(n-2*i-2))

resy = 10**18
tmp = 0
for i in range(n):
    tmp += y[i]
    sumy -= y[i]
    resy = min(resy, sumy-tmp-y[i]*(n-2*i-2))

print(resx+resy)
