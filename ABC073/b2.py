n = int(input())
res = 0
for i in range(n):
    r, l = map(int, input().split())
    res += l - r + 1
print(res)
