import sys
import os


def main():
    dir_path = sys.argv[1]
    os.makedirs(dir_path, exist_ok=True)

    lines = [
        "import sys\n",
        "sys.setrecursionlimit(10**7)\n",
        "input = sys.stdin.readline\n",
        "\n"
    ]

    for i in "abcde":
        with open(os.path.join(dir_path, f"{i}.py"), "x") as f:
            f.writelines(lines)


if __name__ == "__main__":
    main()
