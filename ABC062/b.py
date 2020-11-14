h, w = map(int, input().split())
pic = [input() for i in range(h)]

for i in range(h + 2):
    res = ""
    for j in range(w + 2):
        if i == 0 or i == h + 1 or j == 0 or j == w + 1:
            res += "#"
        else:
            res += pic[i - 1][j - 1]
    print(res)
