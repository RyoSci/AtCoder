h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

res = 0
for i in range(h-1):
    for j in range(w-1):
        tmp = 0
        for ii in range(2):
            for jj in range(2):
                if s[i+ii][j+jj] == "#":
                    tmp += 1
        if tmp == 1 or tmp == 3:
            res += 1
print(res)
