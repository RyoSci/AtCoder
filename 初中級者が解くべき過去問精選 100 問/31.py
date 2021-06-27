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
    queue = deque()
    queue.append((i, j))
    seen = set()
    seen.add((i, j))
    while len(queue) != 0:
        i, j = queue.popleft()
        if i % 2 == 0:
            for di, dj in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]:
                ni = i+di
                nj = j+dj
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == 0 and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        queue.append((ni, nj))
                else:
                    return False
        else:
            for di, dj in [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]:
                ni = i+di
                nj = j+dj
                if 0 <= ni < h and 0 <= nj < w:
                    if grid[ni][nj] == 0 and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        queue.append((ni, nj))
                else:
                    return False

    return True


res = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == 1:
            res += surround(i, j, 1)
        else:
            if judge_inter(i, j):
                res -= surround(i, j, 0)
print(res)
