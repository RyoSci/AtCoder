import queue
n, m = map(int, input().split())
s = [input() for i in range(n)]
dod_sum = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == ".":
            dod_sum += 1

res = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            dot_num = 1
            q = queue.Queue()
            now = (i, j)
            q.put(now)
            double_check = set()
            double_check.add(now)

            while not q.empty():
                # dx = [-1, 0, 1]
                # dy = [-1, 0, 1]
                dx_dy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                now = q.get()
                if now[0] == 0:
                    dx_dy[0] = [0, 0]
                if now[0] == n - 1:
                    dx_dy[1] = [0, 0]
                if now[1] == 0:
                    dx_dy[2] = [0, 0]
                if now[1] == m - 1:
                    dx_dy[3] = [0, 0]
                x, y = now
                for ii in dx_dy:
                    if (x + ii[0], y + ii[1]) not in double_check and s[x + ii[0]][y + ii[1]] == ".":
                        dot_num += 1
                        double_check.add((x + ii[0], y + ii[1]))
                        q.put((x + ii[0], y + ii[1]))
            if dot_num == dod_sum + 1:
                res += 1

print(res)
