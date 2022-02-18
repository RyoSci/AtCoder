from queue import Queue

n = int(input())
ver_vers_dis = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    ver_vers_dis[a - 1].append([b - 1, c])
    ver_vers_dis[b - 1].append([a - 1, c])


distances = [-1] * n


def bfs(pair, dis_from_k):
    queue = Queue()
    queue.put([pair, dis_from_k])
    while not queue.empty():
        pair, dis_from_k = queue.get()
        chi_dis = ver_vers_dis[pair]
        for chi, dis in chi_dis:
            if distances[chi] == -1:
                distances[chi] = dis_from_k + dis
                queue.put([chi, dis_from_k + dis])
    return


q, k = map(int, input().split())
distances[k - 1] = 0
bfs(k - 1, 0)
for i in range(q):
    x, y = map(lambda x: int(x) - 1, input().split())
    print(distances[x] + distances[y])
