import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
ver_edge_len = [[] for i in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    ver_edge_len[u - 1].append([v, w])
    ver_edge_len[v - 1].append([u, w])

ver_colors = [-1] * n
ver_colors[0] = 0


def dfs(pair):
    for chi in ver_edge_len[pair - 1]:
        if ver_colors[chi[0] - 1] == -1:
            ver_colors[chi[0] - 1] = ver_colors[pair - 1] ^ (chi[1] % 2)
            dfs(chi[0])
    return 0


if __name__ == "__main__":
    dfs(1)

    for i in range(n):
        print(ver_colors[i])
