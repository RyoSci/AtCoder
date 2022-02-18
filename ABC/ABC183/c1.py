n, k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]

res = 0


def dfs(a: str, i: int, dis: int):
    global res
    if i == n - 1:
        if dis + t[int(a[-1]) - 1][0] == k:
            res += 1
            return 1
    for j in range(2, n + 1):
        if str(j) not in a:
            dfs(a + str(j), i + 1, dis + t[int(a[-1]) - 1][j - 1])


if __name__ == "__main__":
    dfs("1", 0, 0)
    print(res)
