n = int(input())
d = list(map(int, input().split()))
sum_d = sum(d)

res = 0
for i in range(n):
    sum_d -= d[i]
    res += sum_d*d[i]

print(res)
