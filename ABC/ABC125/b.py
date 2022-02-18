n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

res = 0
for i in range(n):
    if v[i] > c[i]:
        res += v[i] - c[i]

print(res)