from queue import Queue
h, w = map(int, input().split())
masu = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    masu[i][0] = 1
for j in range(w):
    masu[-1][j] = 1
# masu = [[0 for j in range(w)] for i in range(h)]
q = int(input())


def bfs(a, b, c, d):
    if a == c and b == d:
        return True
    pos = set()
    pos.add((a, b))
    que = Queue()
    que.put((a, b))
    while not que.empty():
        x, y = que.get()
        for i, j in ([-1, 0], [0, 1], [1, 0], [0, -1]):
            xx = x+i
            yy = y+j
            if 0 <= xx < h and 0 <= yy < w and masu[xx][yy] == 1:
                if xx == c and yy == d:
                    return True
                if (xx, yy) not in pos:
                    que.put((xx, yy))
                    pos.add((xx, yy))
    else:
        return False


for i in range(q):
    # qi = list(map(int, input().split()))
    qi = (2, 1, 1, 2000, 2000)
    if qi[0] == 1:
        masu[qi[1]-1][qi[2]-1] = 1
    else:
        _, rai, cai, rbi, cbi = qi
        ans = "No"
        if masu[rai-1][cai-1] == 1 and masu[rbi-1][cbi-1] == 1:
            if bfs(rai-1, cai-1, rbi-1, cbi-1):
                ans = "Yes"
        print(ans)
