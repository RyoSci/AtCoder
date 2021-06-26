n, k = map(int, input().split())

res = k*(k+1)//2*n
res += n*(n+1)//2*k*100
print(res)
