# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


INF = 10**18


n = int(input())
x = list(map(int, input().split()))
c = list(map(int, input().split()))


"https://qiita.com/toast-uz/items/bf6f142bace86c525532"

# 有向グラフの典型入力を双方向で適用
adj = [[] for _ in range(n)]
adj_inv = [[] for _ in range(n)]
for a in range(n):
    b = x[a]-1
    adj[a].append(b)
    adj_inv[b].append(a)

seen = [False] * n
finished = [False] * n
backward_list = []


def dfs1(pos):
    todo = deque()
    todo.append(pos)   # 初期探索場所をpush
    while todo:
        pos = todo.pop()   # LIFOでpop
        if finished[pos]:
            continue
        seen[pos] = True
        # 帰りがけの判定
        next_list = [x for x in adj[pos] if not seen[x]]
        if len(next_list) == 0:
            finished[pos] = True
            backward_list.append(pos)
        else:
            todo.append(pos)
            for next_ in next_list:
                todo.append(next_)
    return


for i in range(n):
    if not seen[i]:
        dfs1(i)

seen = [False] * n
groups = defaultdict(list)


def dfs2(pos, label):
    todo = deque()
    todo.append(pos)   # 初期探索場所をpush
    while todo:
        pos = todo.pop()   # LIFOでpop
        if seen[pos]:
            continue
        seen[pos] = True
        groups[label].append(pos)
        # 次の位置を探索する
        for next_ in adj_inv[pos]:
            todo.append(next_)
    return


label = 0
for n in reversed(backward_list):  # 帰りがけの逆順
    if not seen[n]:
        dfs2(n, label)
        label += 1

ans = 0
for k, v in groups.items():
    if len(v) <= 1:
        continue
    res = INF
    for vi in v:
        res = min(res, c[vi])
    ans += res

print(ans)
