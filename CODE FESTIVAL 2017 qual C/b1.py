n = int(input())
a = list(map(int, input().split()))


def dfs(i, res):
    if i == n:
        return (res + 1) % 2

    return dfs(i + 1, (res * (a[i] - 1)) % 2) \
        + dfs(i + 1, (res * a[i]) % 2) \
        + dfs(i + 1, (res * (a[i] + 1)) % 2)


if __name__ == "__main__":
    print(dfs(0, 1))
