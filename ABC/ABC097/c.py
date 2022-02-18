s = input()
k = int(input())


def dfs(t):
    global k
    if k == 0:
        print(t)
        exit()
    for i in range(26):
        if t + chr(ord("a") + i) in s:
            k -= 1
            dfs(t + chr(ord("a") + i))
    return 0


if __name__ == "__main__":
    dfs("")
