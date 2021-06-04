n = int(input())
d = list(map(int, input().split()))
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        res += d[i]*d[j]

print(res)
