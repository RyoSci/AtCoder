h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

res = 0
for i in range(h-1):
    for j in range(w-1):
        if a[i][j] != b[i][j]:
            dis = b[i][j]-a[i][j]
            res += abs(dis)
            for k in range(2):
                for l in range(2):
                    a[i+k][j+l] += dis

total = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != b[i][j]:
            total += 1

if total != 0:
    print("No")
else:
    print("Yes")
    print(res)
