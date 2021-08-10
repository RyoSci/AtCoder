n = int(input())

res = [0]*(n+1)
m = int(n**0.5)
for x in range(1, m+1):
    for y in range(1, m+1):
        for z in range(1, m+1):
            tmp = x**2+y**2+z**2+x*y+y*z+z*x
            if 0 <= tmp <= n:
                res[tmp] += 1

for i in range(n):
    print(res[i+1])
