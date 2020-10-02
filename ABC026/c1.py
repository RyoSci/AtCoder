n = int(input())
b = [[] for i in range(n)]
for i in range(n - 1):
    line = int(input())
    b[line - 1].append(i + 2)


def dfs(i):
    if b[i - 1] == []:
        return 1
    else:
        a = []
        for j in b[i - 1]:
            a.append(dfs(j))
        min_sub = min(a)
        max_sub = max(a)
        return min_sub + max_sub + 1


print(dfs(1))
