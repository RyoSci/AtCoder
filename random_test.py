import random
import subprocess

TESTCASE_FILE = "random.in"
MAIN_FILE = "main.py"
GREEDY_FILE = "greedy.py"


def read_random_case():
    with open(TESTCASE_FILE, "r", encoding="utf-8") as f:
        return "".join(map(str, f.readlines()))


# NOTE: 問題に合わせてランダムテストケースを作成する
def write_random_case():
    with open(TESTCASE_FILE, "w", encoding="utf-8") as f:
        lines = []

        # 1 <= N, K <= 10
        N = 0
        # K = random.randint(-10, 10)
        K = 0
        A = []
        # for i in range(N):
        #     A.append(str(random.randint(-10, 10)))

        lines.append(f"{N}")
        # lines.append(f"{N} {K}")
        # lines.append(" ".join(A))
        # lines.append(f"{N} {K}")
        # lines.append(f"{H} {W} {K}")
        # lines.append(f"{x1} {y1} {x2} {y2}")

        f.write("\n".join(lines))


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


if __name__ == "__main__":
    main()
