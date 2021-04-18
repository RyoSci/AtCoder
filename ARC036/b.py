n = int(input())
h = [int(input()) for _ in range(n)]

down = True
res = 1
start = 0

for i in range(n - 1):
    if h[i] < h[i + 1]:
        if down:
            start = i
        res = max(res, i + 1 - start + 1)
        down = False
    elif h[i] > h[i + 1]:
        res = max(res, i + 1 - start + 1)
        down = True
    else:
        down = True
        start = i + 1

print(res)
