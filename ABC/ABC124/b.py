n = int(input())
h = list(map(int, input().split()))

res = 0
max_h = 0
for i in range(n):
    if h[i] >= max_h:
        res += 1
        max_h = h[i]
print(res)
