import typing
n = int(input())

res = set()
str_num = ""
def dfs(str_num:str, i:int):
    global res
    if i == 10 :
        # print(str_num)
        if str_num and int(str_num) <= n and len(set(str_num)) == 3:
            res.add(str_num)
            # print(res, str_num)
        return 0
    dfs(str_num + "3", i + 1)
    dfs(str_num + "5", i + 1)
    dfs(str_num + "7", i + 1)
    dfs(str_num      , i + 1)

if __name__ == "__main__":
    dfs(str_num, 0)
    print(len(res))
