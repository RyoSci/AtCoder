from queue import Queue
h, w = map(int, input().split())
start = list(map(lambda x: int(x)-1, input().split()))
end = list(map(lambda x: int(x)-1, input().split()))
s = [list(input()) for _ in range(h)]
res = [[10**7 for j in range(w)] for i in range(h)]
res[start[0]][start[1]]
q = Queue()
for i in "udrl":
    q.put([start[0], start[1], 0, i])


while not q.empty():
    x, y, cnt, direction = q.get()
    for [dx, dy], tmp_dir in zip([[-1, 0], [1, 0], [0, 1], [0, -1]], "udrl"):
        if 0 <= x+dx < h and 0 <= y+dy < w and s[x+dx][y+dy] == ".":
            is_not_dir = direction != tmp_dir
            if res[x+dx][y+dy] >= cnt + is_not_dir:
                res[x+dx][y+dy] = cnt+is_not_dir
                q.put([x+dx, y+dy, cnt+is_not_dir, tmp_dir])

print(res[end[0]][end[1]])
