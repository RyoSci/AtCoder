n, k = map(int, input().split())

res = 0
for y in range(2, 2*n+1):
    x = k+y
    if 2 <= x <= 2*n:
        if x <= n:
            if y <= n:
                res += (x-1)*(y-1)
            else:
                res += (x-1)*(2*n-y+1)
        else:
            if y <= n:
                res += (2*n-x+1)*(y-1)
            else:
                res += (2*n-x+1)*(2*n-y+1)

print(res)
