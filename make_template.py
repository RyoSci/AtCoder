import sys
import os


def main():
    dir_path = sys.argv[1]
    os.makedirs(dir_path, exist_ok=True)

    lines = [
        "# import pypyjit\n",
        "# pypyjit.set_param('max_unroll_recursion=-1')\n",
        "import sys\n",
        "sys.setrecursionlimit(10**6)\n",
        "input = sys.stdin.readline\n",
        "INF=10**18",
        "\n"
    ]

    for i in "abcdef":
        with open(os.path.join(dir_path, f"{i}.py"), "x") as f:
            # f.writelines(lines)
            pass

    with open(os.path.join(dir_path, "review.md"), "x") as f:
        for i in "abcdef":
            f.write("- ")
            f.write(i+":\n\n")


if __name__ == "__main__":
    main()
