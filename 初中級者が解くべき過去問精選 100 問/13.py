r, c = map(int, input().split())
senbei = [list(map(int, input().split())) for _ in range(r)]
# senbei = [[0 for j in range(c)] for _ in range(r)]

false_senbei = [[] for _ in range(r)]

for i in range(r):
    for j in range(c):
        false_senbei[i].append(senbei[i][j] ^ 1)

res = 0
for i in range(1 << r):
    tmp = []
    for j in range(r):
        if i >> j & 1:
            tmp.append(false_senbei[j])
        else:
            tmp.append(senbei[j])
    tmp_res = 0
    for jj in range(c):
        reverce_cnt = 0
        for ii in range(r):
            if tmp[ii][jj] == 1:
                reverce_cnt += 1
        tmp_res += max(reverce_cnt, r-reverce_cnt)
    res = max(res, tmp_res)

print(res)
