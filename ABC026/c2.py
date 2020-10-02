n = int(input())
b = [[] for i in range(n)]
for i in range(n - 1):
    line = int(input())
    b[line - 1].append(i + 2)


def dfs(i):
    if b[i - 1] == []:
        return 1
    else:
        min_sub = 10 ** 7
        max_sub = 0
        for j in b[i - 1]:
            a = dfs(j)
            min_sub = min(a, min_sub)
            max_sub = max(a, max_sub)
        return min_sub + max_sub + 1


print(dfs(1))
