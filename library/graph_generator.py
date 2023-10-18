import itertools
import random

# TODO: 有向グラフに対応（DAG か否かの取り扱いにも対応）


class GraphGenerator:
    def __init__(self, v_weight=None, w_weight=None,
                 connected=True, self_edge=False, multi_edge=False):
        if v_weight is not None:
            assert len(v_weight) == 2
            assert v_weight[0] <= v_weight[1]
        if w_weight is not None:
            assert len(w_weight) == 2
            assert w_weight[0] <= w_weight[1]

        self.v_weight = v_weight
        self.w_weight = w_weight
        self.connected = connected
        self.self_edge = self_edge
        self.multi_edge = multi_edge

    def generate_tree(self, N):
        E = [(random.randint(1, i - 1), i) for i in range(2, N + 1)]
        E.sort()
        return E

    def generate_path(self, N):
        E = [(i, i + 1) for i in range(1, N)]
        return E

    def generate_star(self, N):
        E = [(1, i) for i in range(2, N + 1)]
        return E

    def generate_binary_tree(self, N):
        E = [(i // 2, i) for i in range(2, N + 1)]
        return E

    def generate_clique(self, N):
        E = list(itertools.combinations(range(1, N + 1), 2))
        return E

    def generate_graph(self, N, M):
        if self.connected:
            assert N - 1 <= M, f"連結グラフには N - 1 <= M が必要です"
        E = []
        E_set = set(self.generate_tree(N)) if self.connected else set()
        if self.multi_edge:
            E = list(E_set)
            while len(E) < M:
                u = random.randint(1, N)
                v = random.randint(u, N)
                if (not self.self_edge) and (u == v):
                    continue
                E.append((u, v))
        else:
            while len(E_set) < M:
                u = random.randint(1, N)
                v = random.randint(u, N)
                if (not self.self_edge) and (u == v):
                    continue
                E_set.add((u, v))
            E = list(E_set)
        E.sort()
        return E

    def print_graph(self, N, E, skip_M=False):
        if skip_M:
            print(N)
        else:
            print(N, len(E))

        if self.v_weight is not None:
            min_v, max_v = self.v_weight
            print(" ".join(map(str, [random.randint(min_v, max_v) for _ in range(N)])))

        if self.w_weight is None:
            for u, v in E:
                print(u, v)
        else:
            min_w, max_w = self.w_weight
            for u, v in E:
                w = random.randint(min_w, max_w)
                print(u, v, w)


# 使用例
if __name__ == "__main__":
    # 無向グラフ・連結・重みなし
    print("-----------------")
    gg = GraphGenerator()
    N = random.randint(2, 5)
    M = random.randint(N - 1, N * (N - 1) // 2)
    E = gg.generate_graph(N, M)
    gg.print_graph(N, E)

    # 無向グラフ・木・辺の重み
    print("-----------------")
    gg = GraphGenerator(w_weight=(1, 10**3))
    N = random.randint(2, 5)
    E = gg.generate_tree(N)
    gg.print_graph(N, E, skip_M=True)

    # 無向グラフ・連結保証なし・頂点の重み・多重辺
    print("-----------------")
    gg = GraphGenerator(v_weight=(1, 10**3), connected=False, multi_edge=True)
    N = random.randint(2, 5)
    M = random.randint(0, 10)
    E = gg.generate_graph(N, M)
    gg.print_graph(N, E)
