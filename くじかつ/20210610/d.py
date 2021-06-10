n = int(input())
res = 0

for i in range(1, n+1):
    res += (i+n//i*i)*(n//i)//2

print(res)
