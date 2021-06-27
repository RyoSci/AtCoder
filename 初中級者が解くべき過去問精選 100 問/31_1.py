from collections import deque
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]


def surround(i, j, zero_one):
    tmp = 0
    if i % 2 == 0:
        for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]:
            ni = i+di
            nj = j+dj
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] != zero_one:
                    tmp += 1
            else:
                tmp += 1
    else:
        for di, dj in [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]:
            ni = i+di
            nj = j+dj
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] != zero_one:
                    tmp += 1
            else:
                tmp += 1
    return tmp


def judge_inter(i, j):
    if seen[i][j] != -1:
        return seen[i][j]
    queue = deque()
    queue.append((i, j))
    tmp = set()
    tmp.add((i, j))
    flag = True
    while len(queue) != 0:
        i, j = queue.popleft()
        if i % 2 == 0:
            for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]:
                ni = i+di
                nj = j+dj
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == 0 and (ni, nj) not in tmp:
                        tmp.add((ni, nj))
                        queue.append((ni, nj))
                else:
                    flag = False
        else:
            for di, dj in [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]:
                ni = i+di
                nj = j+dj
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == 0 and (ni, nj) not in tmp:
                        tmp.add((ni, nj))
                        queue.append((ni, nj))
                else:
                    flag = False
    if flag:
        for (ii, jj) in list(tmp):
            seen[ii][jj] = True
    else:
        for (ii, jj) in list(tmp):
            seen[ii][jj] = False

    return flag


seen = [[-1] * w for _ in range(h)]
res = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 1:
            res += surround(i, j, 1)
        else:
            if judge_inter(i, j):
                res -= surround(i, j, 0)
print(res)
