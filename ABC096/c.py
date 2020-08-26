h, w = map(int, input().split())
s = []
for i in range(h):
    si = list(input())
    s.append(si)

ans = True
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            u_r_d_l = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            if i == 0:
                u_r_d_l[0] = (0, 0)
            if i == h - 1:
                u_r_d_l[2] = (0, 0)
            if j == 0:
                u_r_d_l[3] = (0, 0)
            if j == w - 1:
                u_r_d_l[1] = (0, 0)
            for k in u_r_d_l:
                if k != (0, 0):
                    if s[i + k[0]][j + k[1]] == "#":
                        # ans = True
                        break
            else:
                ans = False


if ans:
    print("Yes")
else:
    print("No")
