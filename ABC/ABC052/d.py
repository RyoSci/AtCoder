n, a, b = map(int, input().split())
x = list(map(int, input().split()))
res = 0

for i in range(n - 1):
    res += min(b, (x[i + 1] - x[i]) * a)

print(res)
