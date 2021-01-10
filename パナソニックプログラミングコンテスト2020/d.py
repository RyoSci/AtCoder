n = int(input())


def dfs(s, smax):
    if len(s) == n:
        print(s)
        return 0
    i = ord("a")
    while i <= smax + 1:
        dfs(s + chr(i), max(smax, i))
        i += 1


if __name__ == "__main__":
    dfs("a", ord("a"))
