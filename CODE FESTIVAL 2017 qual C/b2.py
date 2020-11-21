n = int(input())
a = list(map(int, input().split()))


def dfs(i, res):
    if i == n:
        return (res + 1) % 2
    tmp_sum = 0
    for j in range(-1, 2, 1):
        tmp_sum += dfs(i + 1, (res * (a[i] + j) % 2))

    return tmp_sum


if __name__ == "__main__":
    print(dfs(0, 1))
