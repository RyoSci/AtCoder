h, w = map(int, input().split())
s = [input() for i in range(h)]

change_nums = [[-1 for i in range(w)] for i in range(h)]
res = 10 ** 4


def dfs(x, y, before_color, n):
    global res
    if before_color != s[x][y]:
        n += 1
    if x == h - 1 and y == w - 1:
        res = min(res, n)
        return n
    if change_nums[x][y] != -1:
        n += change_nums[x][y]
        return n
    elif x == h - 1:
        a = dfs(x, y + 1, s[x][y], n)
    elif y == w - 1:
        a = dfs(x + 1, y, s[x][y], n)
    else:
        a = min(dfs(x, y + 1, s[x][y], n), dfs(x + 1, y, s[x][y], n))
    change_nums[x][y] = a - n
    return a


if __name__ == "__main__":
    ans = (dfs(0, 0, ".", 0) + 1) // 2
    print(ans)
