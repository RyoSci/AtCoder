from queue import Queue
import time

tik = time.time()


n = int(input())
space = [[0 for i in range(10 ** 4)] for j in range(10 ** 4)]

ans = []
for i in range(n):
    x, y, r = map(int, input().split())
    space[x][y] = 1
    ans.append([r, i, x, y, x, y])

ans.sort(reverse=True)

q = Queue()
for i in range(n):
    q.put([ans[i][1], ans[i][2], ans[i][3], ans[i][4], ans[i][5]])

ans.sort(key=lambda x: x[1])


def timer(tik):
    if time.time() - tik > 4.8:
        for i in range(n):
            print(ans[i][2], ans[i][3], ans[i][4], ans[i][5])
        exit()


while not q.empty():
    i, a, b, c, d = q.get()
    # print(i, a, b, c, d)

    flag = False
    if 0 <= a - 1 and space[a - 1][b] == 0:
        for j in range(b, d + 1):
            if space[a - 1][j] == 1:
                break
        else:
            a -= 1
            for j in range(b, d + 1):
                space[a][j] = 1
            timer(tik)
            ans[i][2] = a
            flag = True

    if 0 <= b - 1 and space[a][b - 1] == 0:
        for j in range(a, c + 1):
            if space[j][b - 1] == 1:
                break
        else:
            b -= 1
            for j in range(a, c + 1):
                space[j][b] = 1
            timer(tik)
            ans[i][3] = b
            flag = True

    if c + 1 < 10000 and space[c + 1][d] == 0:
        for j in range(b, d + 1):
            if space[c + 1][j] == 1:
                break
        else:
            c += 1
            for j in range(b, d + 1):
                space[c][j] = 1
            timer(tik)
            ans[i][4] = c
            flag = True

    if d + 1 < 10000 and space[c][d] == 0:
        for j in range(a, c + 1):
            if space[j][d + 1] == 1:
                break
        else:
            d += 1
            for j in range(a, c + 1):
                space[j][d] = 1
            timer(tik)
            ans[i][5] = d
            flag = True
    if flag:
        q.put([i, a, b, c, d])

    if time.time() - tik < 4.5:
        break
