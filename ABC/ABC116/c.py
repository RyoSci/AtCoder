n = int(input())
h = list(map(int, input().split()))
h = [0] + h

res = 0
for i in range(n):
    res += max(h[i + 1] - h[i], 0)

print(res)
