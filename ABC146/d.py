
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

pair_chi_edgeid = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    pair_chi_edgeid[a].append([b, i])
    pair_chi_edgeid[b].append([a, i])

colors = 0
for i in range(n):
    if colors < len(pair_chi_edgeid[i]):
        colors = len(pair_chi_edgeid[i])

ans = [-1] * (n - 1)


def dfs(chi, edge_color):
    for grand_chi, edgeid in pair_chi_edgeid[chi]:
        if ans[edgeid] == -1:
            edge_color += 1
            edge_color %= colors
            ans[edgeid] = edge_color
            dfs(grand_chi, edge_color)
    return


if __name__ == "__main__":
    dfs(0, 0)
    print(colors)
    for i in range(n - 1):
        print(ans[i] + 1)
