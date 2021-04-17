import copy
a = [list(input()) for _ in range(10)]

res = 0
for i in range(10):
    for j in range(10):
        if a[i][j] == "o":
            res += 1


def dfs(i, j):
    global cnt
    for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        if 0 <= i + di < 10 and 0 <= j + dj < 10:
            if a_[i + di][j + dj] == "o":
                a_[i + di][j + dj] = "x"
                cnt += 1
                dfs(i + di, j + dj)
    return cnt                

ans = "NO"
for i in range(10):
    for j in range(10):
        if a[i][j] == "o":
            continue
        a_ = copy.deepcopy(a)
        cnt = 0
        cnt = dfs(i, j)
        if res == cnt:
            ans = "YES"
            print(ans)
            exit()

print(ans)