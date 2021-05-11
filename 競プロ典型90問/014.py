n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

res = 0
for i in range(n):
    res += abs(a[i]-b[i])

print(res)
