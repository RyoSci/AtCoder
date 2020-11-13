n = int(input())
k = int(input())
x = list(map(int, input().split()))

res = 0
for i in range(n):
    res += min(x[i], k - x[i]) * 2


print(res)
