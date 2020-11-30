import queue
h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

xy = (0, 0)
q = queue.Queue()
q.put(xy)
trace = [["." for i in range(w)] for j in range(h)]
trace[xy[0]][xy[1]] = "#"
while not q.empty():
    x, y = q.get()
    if x + 1 < h and a[x + 1][y] == "#":
        q.put((x + 1, y))
        trace[x + 1][y] = "#"
    elif y + 1 < w and a[x][y + 1] == "#":
        q.put((x, y + 1))
        trace[x][y + 1] = "#"

if trace == a:
    print("Possible")
else:
    print("Impossible")
