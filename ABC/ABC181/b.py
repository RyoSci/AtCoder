n = int(input())
res = 0
for i in range(n):
    a, b = map(int, input().split())
    res += (a + b) * (b - a + 1) // 2

print(res)
