from collections import deque

while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    var = []
    hor = []
    for i in range(2*h-1):
        line = input().split()
        if i % 2 == 0:
            var.append(line)
        else:
            hor.append(line)
    queue = deque()
    queue.append((0, 0))
    seen = [[0]*w for _ in range(h)]
    seen[0][0] = 1
    while len(queue) != 0:
        i, j = queue.popleft()
        cnt = seen[i][j]
        if i == h-1 and j == w-1:
            print(cnt)
            break
        for [di, dj], [ii, jj] in zip([[0, 1], [0, -1], [1, 0], [-1, 0]], [[i, j], [i, j-1], [i, j], [i-1, j]]):
            ni = i+di
            nj = j+dj
            if 0 <= ni < h and 0 <= nj < w and seen[ni][nj] == 0:
                if di == 0:
                    if 0 <= ii < h and 0 <= jj < w-1 and var[ii][jj] == "0":
                        queue.append((ni, nj))
                        seen[ni][nj] = cnt+1
                else:
                    if 0 <= ii < h-1 and 0 <= jj < w and hor[ii][jj] == "0":
                        queue.append((ni, nj))
                        seen[ni][nj] = cnt+1
    else:
        print(0)
