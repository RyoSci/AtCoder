h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

ans = "Impossible"
trace = [["." for i in range(w)] for _ in range(h)]
trace[0][0] = "#"
trace[h - 1][w - 1] = "#"


def mark(x, y):
    trace[x][y] = "#"
    dfs(x, y)
    trace[x][y] = "."


def dfs(x, y):
    global ans
    if x == h - 1 and y == w - 1:
        if trace == a:
            ans = "Possible"
    elif x == h - 1:
        mark(x, y + 1)
    elif y == w - 1:
        mark(x + 1, y)
    else:
        mark(x, y + 1)

        mark(x + 1, y)


if __name__ == "__main__":
    dfs(0, 0)
    print(ans)
