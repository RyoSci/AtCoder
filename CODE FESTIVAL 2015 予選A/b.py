n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    res += a[i]*(2**(n-i-1))

print(res)
