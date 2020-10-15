import queue
r, c = map(int, input().split())
start = list(map(int, input().split()))
goal = list(map(int, input().split()))
maze = [input() for i in range(r)]

q = queue.Queue()
q.put([start, 0])
op = [[1, 0], [0, 1], [-1, 0], [0, -1]]
root = set()
root.add((start[0], start[1]))
while not q.empty():
    y_x, num = q.get()
    y, x = y_x[0], y_x[1]
    if y == goal[0] and x == goal[1]:
        print(num)
        break
    for i in op:
        if y + i[0] - 1 < 0 or y + i[0] - 1 >= r or x + i[1] - 1 < 0 or x + i[1] - 1 >= c:
            continue
        elif maze[y + i[0] - 1][x + i[1] - 1] == ".":
            if (y + i[0], x + i[1]) not in root:
                q.put([[y + i[0], x + i[1]], num + 1])
                root.add((y + i[0], x + i[1]))
