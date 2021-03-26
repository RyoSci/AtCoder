n = int(input())
res = 0
for i in range(n):
    a, b = map(int, input().split())
    res += a * b * 1.05

print(int(res))
