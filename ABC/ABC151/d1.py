h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0


def dfs(i, j, num, i_, j_, passed):
    global ans
    # i_ = []
    # j_ = []
    if i - 1 >= 0:
        i_.append(i - 1)
        j_.append(j)
    if i + 1 <= h - 1:
        i_.append(i + 1)
        j_.append(j)
    if j - 1 >= 0:
        i_.append(i)
        j_.append(j - 1)
    if j + 1 <= w - 1:
        i_.append(i)
        j_.append(j + 1)
    for i, j in zip(i_, j_):
        if s[i][j] == "." and (i, j) not in passed:
            passed.add((i, j))
            memo[i][j] = min(memo[i][j], num + 1)
            # ans = max(ans, memo[i][j])
            dfs(i, j, num + 1, [], [], passed)


for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            memo = [[100000 for ii in range(w)] for jj in range(h)]
            memo[i][j] = 0
            num = 0
            passed = set()
            passed.add((i, j))
            dfs(i, j, num, [], [], set((i, j)))
            for ii in range(h):
                for jj in range(w):
                    ans = max(ans, memo[ii][jj])

print(ans)
