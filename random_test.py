import itertools
import random
import subprocess

TESTCASE_FILE = "random.in"
MAIN_FILE = "main.py"
GREEDY_FILE = "greedy.py"


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
            print(
                " ".join(map(str, [random.randint(min_v, max_v) for _ in range(N)])))

        if self.w_weight is None:
            for u, v in E:
                print(u, v)
        else:
            min_w, max_w = self.w_weight
            for u, v in E:
                w = random.randint(min_w, max_w)
                print(u, v, w)


def read_random_case():
    with open(TESTCASE_FILE, "r", encoding="utf-8") as f:
        return "".join(map(str, f.readlines()))


# NOTE: 問題に合わせてランダムテストケースを作成する
def write_random_case():
    with open(TESTCASE_FILE, "w", encoding="utf-8") as f:

        n = random.randint(2, 20)
        d = []
        for i in range(n):
            d.append(chr(ord("A")+random.randint(0, 25)))

        d = "".join(d)

        f.write(d + "\n")


def solve(proc_name):
    with open(TESTCASE_FILE, "r", encoding="utf-8") as f:
        res = subprocess.run(
            ["python3", proc_name], stdin=f, stdout=subprocess.PIPE, encoding="utf-8")
        return res.stdout


def main():
    while True:
        write_random_case()
        A = solve(MAIN_FILE)
        B = solve(GREEDY_FILE)
        if A != B:
            print("----------------------------------------")
            print("Wrong Answer")
            print("[test case]")
            print(read_random_case())
            print(f"[{MAIN_FILE}]")
            print(A, end="")
            print(f"[{GREEDY_FILE}]")
            print(B, end="")
            print("----------------------------------------")
            break


if __name__ == "__main__":
    main()
