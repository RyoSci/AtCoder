n, x = map(int, input().split())


def dfs(n, cnt, pati):
    if n == 1:
        if cnt + 1 == x:
            return pati
        elif cnt + 2 == x:
            return pati + 1
        elif cnt + 3 == x:
            return pati + 2
        elif cnt + 4 == x:
            return pati + 3
        elif cnt + 5 == x:
            return pati + 3

    if cnt + 1 == x:
        return pati
    cnt += 1
    if x <= cnt + 2 ** (n + 1) - 3:
        return dfs(n - 1, cnt, pati)
    cnt += 2 ** (n + 1) - 3
    pati += 2 ** n - 1
    if cnt + 1 == x:
        return pati + 1
    cnt += 1
    pati += 1
    if x <= cnt + 2 ** (n + 1) - 3:
        return dfs(n - 1, cnt, pati)
    cnt += 2 ** (n + 1) - 3
    pati += 2 ** n - 1
    if cnt + 1 == x:
        return pati


if __name__ == "__main__":
    print(dfs(n, 0, 0))
