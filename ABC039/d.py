h, w = map(int, input().split())
pic = [list(input()) for i in range(h)]
res = [["." for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        i_u = max(i - 1, 0)
        i_d = min(i + 1, h - 1)
        j_l = max(j - 1, 0)
        j_r = min(j + 1, w - 1)
        flag = True
        for ii in range(i_u, i_d + 1):
            for jj in range(j_l, j_r + 1):
                if pic[ii][jj] == ".":
                    flag = False
                    break
            if not flag:
                break
        else:
            res[i][j] = "#"

check = [["." for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if res[i][j] == "#":
            i_u = max(i - 1, 0)
            i_d = min(i + 1, h - 1)
            j_l = max(j - 1, 0)
            j_r = min(j + 1, w - 1)
            for ii in range(i_u, i_d + 1):
                for jj in range(j_l, j_r + 1):
                    check[ii][jj] = "#"

if pic == check:
    print("possible")
    for i in range(h):
        print("".join(res[i]))
else:
    print("impossible")
