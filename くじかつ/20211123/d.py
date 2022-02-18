import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b, k = map(int, input().split())


def cal(n, k):
    res = 1
    for i in range(n+k, n, -1):
        res *= i
    for i in range(k, 0, -1):
        res //= i
    return res


res = ""


def dfs(a, b, now):
    global res
    if a == 0 and b == 0:
        return
    # aを使う場合
    a_start = now
    a_end = a_start+cal(a-1, b)-1

    # bを使う場合
    b_start = a_end+1
    b_end = b_start+cal(a, b-1)-1

    if a_start <= k <= a_end:
        res += "a"
        dfs(a-1, b, a_start)
    else:
        res += "b"
        dfs(a, b-1, b_start)


dfs(a, b, 1)
print(res)
