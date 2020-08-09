import typing
n = int(input())

res = 0
str_num = ""


def dfs(str_num: str, i: int, finish:int):
    global res
    if i == finish:
        # print(str_num)
        if str_num and int(str_num) <= n and len(set(str_num)) == 3:
            res += 1
            # print(res, str_num)
        return 0
    dfs(str_num + "3", i + 1, finish)
    dfs(str_num + "5", i + 1, finish)
    dfs(str_num + "7", i + 1, finish)
    # dfs(str_num, i + 1)


if __name__ == "__main__":
    for i in range(3, 10):
        dfs(str_num, 0, i)
    print(res)
