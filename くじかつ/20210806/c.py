n, m = map(int, input().split())
a = 1-(1/2)**m
res = int((1/(1-a))**2 * (1800*m+100*n)*(1/2)**m)
print(res)
