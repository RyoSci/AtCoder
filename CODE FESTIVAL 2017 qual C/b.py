n = int(input())
a = list(map(int, input().split()))

ans = 0


def dfs(i, res):
    global ans
    if i == n:
        if res % 2 == 0:
            ans += 1
        return 0
    for j in range(-1, 2, 1):
        dfs(i + 1, res*(a[i] + j))


if __name__ == "__main__":
    dfs(0, 1)
    print(ans)
